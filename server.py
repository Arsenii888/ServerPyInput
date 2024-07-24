import socket
import keyboard
import mouse
import vgamepad as vg

gamepad = vg.VX360Gamepad()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5050))
s.listen(5)
data=0
print('Server is listening'+" localhost:5050")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    request = c.recv(1024)
    if request[0]==0:
        keyboard.press("q")
    if request[0]==1:
        keyboard.press("w")
    if request[0]==2:
        keyboard.press("e")
    if request[0]==3:
        keyboard.press("r")
    if request[0]==4:
        keyboard.press("t")
    if request[0]==5:
        keyboard.press("y")
    if request[0]==6:
        keyboard.press("u")
    if request[0]==7:
        keyboard.press("i")
    if request[0]==8:
        keyboard.press("o")
    if request[0]==9:
        keyboard.press("p")
    if request[0]==10:
        keyboard.press("a")
    if request[0]==11:
        keyboard.press("s")
    if request[0]==12:
        keyboard.press("d")
    if request[0]==13:
        keyboard.press("f")
    if request[0]==14:
        keyboard.press("g")
    if request[0]==15:
        keyboard.press("h")
    if request[0]==16:
        keyboard.press("j")
    if request[0]==17:
        keyboard.press("k")
    if request[0]==18:
        keyboard.press("l")
    if request[0]==19:
        keyboard.press("z")
    if request[0]==20:
        keyboard.press("x")
    if request[0]==21:
        keyboard.press("c")
    if request[0]==22:
        keyboard.press("v")
    if request[0]==23:
        keyboard.press("b")
    if request[0]==24:
        keyboard.press("n")
    if request[0]==25:
        keyboard.press("m")
    if request[0]==26:
        keyboard.press("left alt")
    if request[0]==27:
        keyboard.press("right alt")
    if request[0]==28:
        keyboard.press("left ctrl")
    if request[0]==29:
        keyboard.press("right ctrl")
    if request[0]==30:
        keyboard.press("space")
    if request[0]==31:
        keyboard.press("esc")
    if request[0]==32:
        keyboard.press("enter")
    if request[0]==33:
        keyboard.press("backspace")
    if request[0]==34:
        keyboard.press("tab")
    if request[0]==35:
        keyboard.press("delete")
    if request[0]==36:
        keyboard.press("insert")
    if request[0]==37:
        keyboard.press("home")
    if request[0]==38:
        keyboard.press("end")
    if request[0]==39:
        keyboard.press("up")
    if request[0]==40:
        keyboard.press("down")
    if request[0]==41:
        keyboard.press("left")
    if request[0]==42:
        keyboard.press("right")
    if request[0]==43:
        keyboard.press("page up")
    if request[0]==44:
        keyboard.press("page down")
    if request[0]==45:
        keyboard.press("0")
    if request[0]==46:
        keyboard.press("1")
    if request[0]==47:
        keyboard.press("2")
    if request[0]==48:
        keyboard.press("3")
    if request[0]==49:
        keyboard.press("4")
    if request[0]==50:
        keyboard.press("5")
    if request[0]==51:
        keyboard.press("6")
    if request[0]==52:
        keyboard.press("7")
    if request[0]==53:
        keyboard.press("8")
    if request[0]==54:
        keyboard.press("9")
    if request[0]==55:
        keyboard.press("f1")
    if request[0]==56:
        keyboard.press("f2")
    if request[0]==57:
        keyboard.press("f3")
    if request[0]==58:
        keyboard.press("f4")
    if request[0]==58:
        keyboard.press("f5")
    if request[0]==59:
        keyboard.press("f6")
    if request[0]==60:
        keyboard.press("f7")
    if request[0]==61:
        keyboard.press("f8")
    if request[0]==62:
        keyboard.press("f9")
    if request[0]==63:
        keyboard.press("f10")
    if request[0]==64:
        keyboard.press("f11")
    if request[0]==65:
        keyboard.press("f12")
    if request[0]==66:
        keyboard.press("num 0")
    if request[0]==67:
        keyboard.press("num 1")
    if request[0]==68:
        keyboard.press("num 2")
    if request[0]==69:
        keyboard.press("num 3")
    if request[0]==70:
        keyboard.press("num 4")
    if request[0]==71:
        keyboard.press("num 5")
    if request[0]==72:
        keyboard.press("num 6")
    if request[0]==73:
        keyboard.press("num 7")
    if request[0]==74:
        keyboard.press("num 8")
    if request[0]==75:
        keyboard.press("num 9")
    if request[0]==76:
        keyboard.press("num *")
    if request[0]==77:
        keyboard.press("num /")
    if request[0]==78:
        keyboard.press("num +")
    if request[0]==79:
        keyboard.press("num -")
    if request[0]==80:
        keyboard.press("num enter")
    if request[0]==81:
        keyboard.press("num .")
    if request[0]==82:
        keyboard.press("caps lock")
    if request[0]==83:
        keyboard.press("screen lock")
    if request[0]==84:
        keyboard.press("print screen")
    if request[0]==85:
        keyboard.press("pause")
    if request[0]==86:
        mouse.press("left")
    if request[0]==87:
        mouse.press("right")
    if request[0]==88:
        mouse.press("middle")
    if request[0]==89:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    if request[0]==90:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    if request[0]==91:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    if request[0]==92:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    
    print(str(request[0]))
        
    c.close()
