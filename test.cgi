#!/usr/bin/env python3
import os
print('Content-type: text/html\r\n\r')
thelist = [ name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name)) ]
print(thelist)