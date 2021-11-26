#!/usr/bin/env python3
import os
print('Content-type: text/html\r\n\r')
folder = './ingredients'

sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

print(sub_folders[0])