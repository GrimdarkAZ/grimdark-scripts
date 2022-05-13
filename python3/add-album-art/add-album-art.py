#!/usr/bin/env python3

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import os,argparse

description = """
Generic Script
--------------
Script to add album art to MP3 file.
"""

import sys
import argparse


def main(argv):
    args = cli(argv)

    audio_path = args.audio
    picture_path = args.image
    audio = MP3(audio_path, ID3=ID3)
    # adding ID3 tag if it is not present
    try:
        audio.add_tags()
    except error:
        pass
    audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(picture_path,'rb').read()))
    # edit ID3 tags to open and read the picture from the path specified and assign it
    audio.save()  # save the current changes


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass


def cli(argv):
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description=description,
        formatter_class=CustomFormatter)

    parser.add_argument(
        "--image",
        type=str,
        help="Path to image")

    parser.add_argument(
        "--audio",
        type=str,
        help="Path to MP3 file")

    args = parser.parse_args(argv[1:])

    return args


if __name__ == '__main__':
    sys.exit(main(sys.argv))