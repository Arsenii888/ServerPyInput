<h1> OpenPyInput </h1>
OpenPyInput is a small server for emulating keyboard input. To use it, you need a client that sends requests.
<h1> How to modify </h1>
To modify it, you need to add a code similar to the one presented:
```python
if request[0]==3:
        keyboard.press("d")
```
If you can, rewrite the server in c++ for better performance
