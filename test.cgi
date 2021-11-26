#!/usr/bin/env python3
import os
folder = './ingredients'

sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

print(sub_folders)