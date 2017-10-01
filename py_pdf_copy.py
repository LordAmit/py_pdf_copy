#!/usr/bin/python

import subprocess
import os
import shlex

content = subprocess.check_output(
    shlex.split('/usr/bin/xsel --clipboard -o')).decode()

contents = content.splitlines()
merged  = ""

for content in contents[1:]:
    merged = merged + " " + content
merged = contents[0] + merged

process = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
process.communicate(input=merged.encode())
