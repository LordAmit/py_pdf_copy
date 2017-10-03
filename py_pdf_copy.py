#!/usr/bin/python3.6

import subprocess
import os
import shlex
import process as p


content = subprocess.check_output(
    shlex.split('/usr/bin/xsel --clipboard -o')).decode('utf-8')

merged = p.process_content(content)

# print(merged)
process = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
process.communicate(input=merged.encode('utf-8'))
