#!env python3

import subprocess
import shlex
import os
import process as p
from abc import ABC, abstractmethod


class AClipBoardManager(ABC):
    @abstractmethod
    def clip_get_content(self) -> bytes:
        pass

    @abstractmethod
    def clip_set_content(self, value: bytes):
        pass


class Xsel(AClipBoardManager):
    def clip_get_content(self) -> bytes:
        return subprocess.check_output(
            shlex.split('/usr/bin/xsel --clipboard -o'))

    def clip_set_content(self, value: bytes):
        process = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
        process.communicate(input=value)


class XClip(AClipBoardManager):
    def clip_get_content(self) -> bytes:
        return subprocess.check_output(
            shlex.split('/usr/bin/xclip -selection clipboard -o '))

    def clip_set_content(self, value: bytes):
        subprocess.Popen(
            shlex.split("/usr/bin/xclip -selection clipboard -i"), stdin=subprocess.PIPE, shell=True).communicate(
            input=value)


class Clipit(AClipBoardManager):

    def clip_get_content(self) -> bytes:
        return subprocess.check_output(
            shlex.split('/usr/bin/clipit -c'))

    def clip_set_content(self, value: bytes):
        subprocess.Popen(
            ['clipit'], stdin=subprocess.PIPE).communicate(
            input=value)


class FileClip(AClipBoardManager):

    def clip_get_content(self) -> str:
        with open('input.txt', 'r') as file:
            return file.read().encode('utf-8')

    def clip_set_content(self, value: str):
        with open('output.txt', 'w') as file:

            file.write(value.decode('utf-8'))
            file.close()

        # subprocess.Popen(
        #     ['clipit'], stdin=subprocess.PIPE).communicate(
        #     input=value)


def process_copied_contents(clip_object: AClipBoardManager):
    content = clip_object.clip_get_content().decode("utf-8")
    output = p.process_content(content)
    clip_object.clip_set_content(output)


def main():
    if os.path.exists('/usr/bin/clipit'):
        print("using clipit")
        clip_object = Clipit()
    elif os.path.exists('/usr/bin/xsel'):
        print("using xsel")
        clip_object = Xsel()
    elif os.path.exists('/usr/bin/xclip'):
        print("using xclip")
        clip_object = XClip()
    elif os.path.exists('input.txt'):
        print('reading input.txt')
        clip_object = FileClip()
        print('writing output.txt')
    else:
        raise AttributeError('Xsel/Clipit not found.')

    process_copied_contents(clip_object)


if __name__ == '__main__':
    main()
