import socket
import keyboard
Import mouse

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
    print(str(request[0]))
    if request[0]==26:
        mouse.press("left")
    if request[0]==27:
        mouse.press("right")
    if request[0]==28:
        mouse.press("middle")
        
    c.close()