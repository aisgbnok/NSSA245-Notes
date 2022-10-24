#!/usr/bin/env python3

"""
Author: Anthony Swierkosz; ajs2576
Date: 10/24/2022

Performs configuration for a CentOS Stream 9 installation.
Downloads the latest CentOS Stream 9 ISO, unpacks it, adds it as a boot option, then reboots.
"""

from subprocess import call
from urllib.request import urlopen

CENTOS_ISO_URL = 'https://mirrors.centos.org/mirrorlist?path=/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso&redirect=1&protocol=https'
CENTOS_ISO = 'CentOS-Stream-9-latest-x86_64-dvd1.iso'


def download_iso():
    """
    Downloads the CentOS Stream 9 ISO to `/tmp`.

    :return: None
    """
    print('Downloading CentOS Stream 9 ISO...')
    url = urlopen(url=CENTOS_ISO_URL)
    with open(f'/tmp/{CENTOS_ISO}', 'wb') as f:
        f.write(url.read())


def unpack_iso():
    """
    Unpacks the CentOS ISO to `/dev/sdb`.

    :return: None
    """
    print('Unpacking CentOS Stream 9 ISO...')
    call(f'dd if=/tmp/{CENTOS_ISO} of=/dev/sdb bs=512k status=progress', shell=True)


def add_boot_option():
    """
    Adds `/dev/sdb` as a boot option to the grub config.

    :return: None
    """
    print('Adding boot option...')
    # Write the custom grub config
    f = open('/etc/grub.d/40_custom', 'w')
    f.write('menuentry "CentOS Stream 9 Installer" {\n')
    f.write('\tset root=(hd1)\n')
    f.write('\tdrivemap -s hd0 hd1\n')
    f.write('\tchainloader +1\n')
    f.write('}')
    f.close()

    # Update grub
    call('grub2-mkconfig -o /boot/grub2/grub.cfg', shell=True)


def main():
    """
    Downloads the CentOS Stream 9 ISO,
    unpacks it to `/dev/sdb`,
    adds it as a boot option,
    then reboots.

    :return: None
    """
    print('Warning: This script will overwrite /dev/sdb.')
    print('Warning: Use this script at your own risk.')
    download_iso()
    unpack_iso()
    add_boot_option()

    # Reboot
    print('Rebooting...')
    call('reboot', shell=True)


# Only if this file is run directly
if __name__ == '__main__':
    main()
