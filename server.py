import socket
import keyboard

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
        keyboard.press("w")
    if request[0]==1:
        keyboard.press("a")
    if request[0]==2:
        keyboard.press("s")
    if request[0]==3:
        keyboard.press("d")
    print(str(request[0]))
        
    c.close()
