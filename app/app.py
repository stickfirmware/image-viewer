import time

import apps.thirdparty.com_kitki30_image_viewer.display_img as disp

import modules.file_explorer as file_explorer
import modules.button_combos as btn_combos
import modules.os_constants as osc
import modules.popup as popups
import modules.io_manager as io_man
import modules.menus as menus

# Entrypoint
def run():
    tft = io_man.get("tft")
    
    while True:
        menu = menus.menu("Image viewer", [
            ("Browse using explorer", 1),
            ("Info!", 2),
            ("Exit", None)
        ])
        
        if menu == None:
            break
        
        if menu == 1:
            file = file_explorer.run(True, "/")
            if file == None:
                continue
            disp.disp(tft, file)
            
            while not btn_combos.any_btn(["a", "b", "c"]):
                time.sleep(osc.LOOP_WAIT_TIME)
            continue
        
        elif menu == 2:
            popups.show("This app requires images to be converted to .bin format.\nUse https://convert.kitki30.tk/\nOr run converter.py from repo.")
            
    time.sleep(5)