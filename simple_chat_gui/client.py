#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

# Filename: socketClient.py

import socket
import sys
import threading

# Client GUI
from tkinter import *
import Pmw

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

root = Tk()
# textDisplay
textDisplay = Pmw.ScrolledText(root)
textDisplay.pack(expand=1, padx=5, pady=5, side=LEFT)
# textInput
textInput = Pmw.ScrolledText(root)
textInput.pack(expand=1, padx=5, pady=5, side=LEFT)


# Send Button and its callback
def sendMsg(event):
    message = socket.gethostname() + ':' + textInput.get()
    # print (sys.stderr, 'sending "%s"' % message)
    print(message)
    sock.sendall(message.encode())
    textInput.clear()
    # data = sock.recv(100)
    # textDisplay.insert(END, data)
    # print (sys.stderr, 'received "%s"' % data)


sendBtn = Button(root, text="Send")
sendBtn.bind('<Button-1>', sendMsg)
sendBtn.pack(side=LEFT)


def receiveMsg():
    while True:
        data = sock.recv(100)
        print(sys.stderr, 'client received "%s"' % data)
        textDisplay.insert(END, data)


receiveThread = threading.Thread(name='waitForMSG', target=receiveMsg)
receiveThread.start()

root.mainloop()
