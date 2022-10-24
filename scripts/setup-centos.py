#!/usr/bin/env python3

"""
Author: Anthony Swierkosz; ajs2576
Date: 10/24/2022

Downloads CentOS Stream 9, unpacks it to /dev/sdb, and adds it as a boot option.
"""

from urllib.request import urlopen
from subprocess import call
import shutil
from os import path, makedirs


def download_centos():
    """
    Downloads the CentOS Stream 9 ISO.

    :return: None
    """
    url = urlopen(url='https://mirrors.centos.org/mirrorlist?path=/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso&redirect=1&protocol=https')
    with open('/tmp/CentOS-Stream-9-latest-x86_64-dvd1.iso', 'wb') as f:
        f.write(url.read())


def unpack_centos():
    """
    Unpacks the CentOS Stream 9 ISO to /dev/sdb.

    :return: None
    """
    call('dd if=/tmp/CentOS-Stream-9-latest-x86_64-dvd1.iso of=/dev/sdb bs=512k status=progress', shell=True)


def add_boot_option():
    """
    Adds the CentOS Stream 9 boot option to the grub config.

    :return: None
    """
    f = open('/etc/grub.d/40_custom', 'w')
    f.write('menuentry "CentOS Stream 9 Installer" {\n')
    f.write('\tset root=(hd1)\n')
    f.write('\tdrivemap -s hd0 hd1\n')
    f.write('\tchainloader +1\n')
    f.write('}')
    f.close()

    call('grub2-mkconfig -o /boot/grub2/grub.cfg', shell=True)


# Only if this file is run directly
if __name__ == '__main__':
    download_centos()
    unpack_centos()
    add_boot_option()
