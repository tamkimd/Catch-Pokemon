from pynput import keyboard
import pyautogui as gui
from who_is_pkm import classify
import time
import os
gui.FAILSAFE = False
button_pos = {
    "fight" : {"x": 1252, "y": 624},
    "bag" : {"x": 1172, "y": 710},
    "run" : {"x": 1252, "y": 707},  
    "back" : {"x": 1342, "y": 715},  
    "move_1" : {"x": 1180, "y": 608},  
    "move_2" : {"x": 1304, "y": 598},  
    "move_3" : {"x": 1179, "y": 644},  
    "move_4" : {"x": 1296, "y": 641},  
    "poke_balls" : {"x": 1303, "y": 590},  
    "pokeball" : {"x": 1190, "y": 573},  
    "use_ball" : {"x": 1235, "y": 710},  
    "next_pkm" : {"x": 1253, "y": 630},  
    "switch_pkm" : {"x": 1251, "y": 633},  
    "no" : {"x": 1250, "y": 682},  
}

def click(position='', x=0, y=0):
    if position:
        gui.mouseDown(**button_pos.get(position.lower()))
        time.sleep(0.01)
        gui.mouseUp(**button_pos.get(position.lower()))
    else:
        gui.mouseDown(x, y)
        time.sleep(0.01)
        gui.mouseUp(x, y)

def catch():
    click("bag")
    time.sleep(1)
    click("poke_balls")
    time.sleep(1)
    click("pokeball")
    time.sleep(1)
    click("use_ball")
time.sleep(3)
def move_Around():
    gui.keyDown("left")
    time.sleep(0.5)
    gui.keyUp("left")
    time.sleep(0.5)
    
    gui.keyDown("right")
    time.sleep(0.5)
    gui.keyUp("right")
def close(key):
    try:
        k = key.char 
    except:
        k = key.name 
    if k in ['p']:  
        print('END')
        keyboard.Listener.stop
        os._exit(0)

def main():
    abra_appeared=0
    abra_catched=0
    while True:
        if gui.locateOnScreen('images/grass2.png', confidence=0.3) or gui.locateOnScreen('images/grass.png', confidence=0.7) != None :
            print(".....")
            move_Around()
        elif gui.locateOnScreen('images/check_catch.png', confidence=0.9) != None:
            gui.screenshot("images/check.png",(620,45,510,510))
            #,(609,31,515,515)
            pkm=classify("images/check.png")
            if pkm=="abra":  
                abra_appeared+=1
                print("abra_Appeared",abra_appeared)
                catch()
                time.sleep(10)
                while True:
                    if gui.locateOnScreen('images/grass2.png', confidence=0.3) or gui.locateOnScreen('images/grass.png', confidence=0.7) != None :
                        break
                    elif gui.locateOnScreen('images/new_pokemon.png', confidence=0.8) != None:
                        abra_catched+=1
                        print("catched:",abra_catched)
                        click("no")
                        time.sleep(2)
                        click("no")
                        time.sleep(1)
                        click("no")
                        break
                    elif gui.locateOnScreen('images/rename_pkm.PNG', confidence=0.9) != None :
                        abra_catched+=1
                        print("catched:",abra_catched)
                        click("no")
                        time.sleep(1)
                        click("no")
                        break
            else:
                print("other")
                click("run")

listener = keyboard.Listener(on_press=close)
listener.start()
main()