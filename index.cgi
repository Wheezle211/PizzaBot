#!/usr/bin/python3
print('Content-type: text/html\r\n\r')
import os, makePizza

os.environ["PYTHONIOENCODING"] = "utf-8"

loc = os.path.dirname(os.path.abspath(__file__))

message = makePizza.makePizza(loc, False)[0]
print(message)
