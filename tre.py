from threading import *
import os
import socket
import re
import math

os.system("clear")

p = input("enter target id : ")

class a(Thread):
    def run(self):
        while True:
            print("sending report to target..")
            os.system("sleep 2")
            print("sending report to target..")
            os.system("sleep 1")

class b(Thread):
    def run(self):
        while True:
            print("sending report to target(1)..")
            os.system("sleep 1")
            print("sending report to target(1)..")
            os.system("sleep 2")

t1 = a()
t2 = b()
t3 = a()
t4 = b()

t1.start()
t2.start()
t3.start()
t4.start()
