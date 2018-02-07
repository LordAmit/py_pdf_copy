#!/usr/bin/python3.6

import subprocess
import shlex
import os
import process as p
from abc import ABC, abstractmethod


class AClipBoardManager(ABC):
    @abstractmethod
    def clip_get_content(self)-> str:
        pass

    @abstractmethod
    def clip_set_content(self, value: str):
        pass


class Xsel(AClipBoardManager):
    def clip_get_content(self)-> str:
        return subprocess.check_output(
            shlex.split('/usr/bin/xsel --clipboard -o')).decode('utf-8')

    def clip_set_content(self, value: str):
        subprocess.Popen(
            ['xsel', '-bi'], stdin=subprocess.PIPE, shell=True).communicate(
            input=value.encode('utf-8'))


class Clipit(AClipBoardManager):

    def clip_get_content(self)->str:
        return subprocess.check_output(
            shlex.split('/usr/bin/clipit -c')).decode('utf-8')

    def clip_set_content(self, value: str):
        subprocess.Popen(
            ['clipit'], stdin=subprocess.PIPE).communicate(
            input=value.encode('utf-8'))


def process_copied_contents(clip_object: AClipBoardManager):
    clip_object.clip_set_content(
        p.process_content(clip_object.clip_get_content()))


def main():
    if os.path.exists('/usr/bin/clipit'):
        clip_object = Clipit()
    elif os.path.exists('/usr/bin/xsel'):
        clip_object = Xsel()
    else:
        raise AttributeError('Xsel/Clipit not found.')

    process_copied_contents(clip_object)


if __name__ == '__main__':
    main()
