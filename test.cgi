#!/usr/bin/env python3
import os
print('Content-type: text/html\r\n\r')
folder = './ingredients'

dick = {
    "butt": "ass",
    "horse": "mare",
    "poop": "pee"
}

john = list(dick)
print(john)

# sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
# for name in sub_folders:
#     completeName = os.path.join('./ingredients/' + name, name + '.txt')
#     print(name)
#     print(completeName)
    #file1 = open(completeName, 'w')
    #file1.write("")
    #file1.close()