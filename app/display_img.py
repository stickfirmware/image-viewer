"""
Module to display .bin images, need to convert first
"""

def disp(tft, file, chunks=27):
    height = 135
    width = 240
    chunk_h = height // chunks

    with open(file, "rb") as f:
        for chunk_id in range(chunks):
            # Get chunk size
            buf_size = width * chunk_h * 2
            buf = bytearray(buf_size)

            # Get file
            start_pix = chunk_id * chunk_h * width
            start_byte = start_pix // 2  # 2 pixels 1 byte
            f.seek(start_byte)
            data = f.read(width * chunk_h // 2)

            for i in range(width * chunk_h):
                pix_idx = i
                byte_idx = pix_idx // 2
                if pix_idx % 2 == 0:
                    gray4 = (data[byte_idx] >> 4) & 0x0F
                else:
                    gray4 = data[byte_idx] & 0x0F
                gray8 = gray4 * 17
                color = (gray8 >> 3 << 11) | (gray8 >> 2 << 5) | (gray8 >> 3)
                buf[i*2]   = color >> 8
                buf[i*2+1] = color & 0xFF

            tft.blit_buffer(buf, 0, chunk_id * chunk_h, width, chunk_h)