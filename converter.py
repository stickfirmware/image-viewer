"""
Image converter for stick firmware
"""

from PIL import Image

# Load image
img = Image.open(str(input("Source image name: ")))
img = img.resize((240, 135), Image.LANCZOS)
img = img.convert("L")  # grayscale

# Convert to 16 shades of gray
def quantize_16(pixel):
    return pixel * 15 // 255

pixels = img.load()

byte_data = bytearray()
for y in range(img.height):
    for x in range(0, img.width, 2):
        p1 = quantize_16(pixels[x, y])
        if x+1 < img.width:
            p2 = quantize_16(pixels[x+1, y])
        else:
            p2 = 0
        # Put two pixels in one byte (Idk how it works)
        byte = (p1 << 4) | p2
        byte_data.append(byte)

with open("image.bin", "wb") as f:
    f.write(byte_data)

print("Done, saved to image.bin")