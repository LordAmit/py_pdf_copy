#!/usr/bin/python3.6

import process as p


a = open('input').read()
# for i in a:
#     print(ord(i))
open('output', 'w').write(p.process_content(a))
