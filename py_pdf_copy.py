#!/usr/bin/python3.6

import subprocess
import shlex
import process as p


def get_content(approach_name) -> str:
    return approach_name()


def post_content(value: str, approach_name) -> None:
    approach_name(value)


xsel_get_content = subprocess.check_output(
    shlex.split('/usr/bin/xsel --clipboard -o')).decode('utf-8')


clipit_get_content = subprocess.check_output(
    shlex.split('/usr/bin/clipit -c')).decode('utf-8')


content = get_content(clipit_get_content)

merged = p.process_content(content)

clipit_post_content = subprocess.Popen(
    ['clipit'], stdin=subprocess.PIPE).communicate(
        input=merged.encode('utf-8'))

xsel_post_content = subprocess.Popen(
    ['xsel', '-bi'], stdin=subprocess.PIPE, shell=True).communicate(
        input=merged.encode('utf-8'))

# print(merged)
# process = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE, shell=True) # noqa
# process.communicate(input=merged.encode('utf-8'))
