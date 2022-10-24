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
    menuentry = open('/etc/grub.d/40_custom', 'w')
    menuentry.write(''.join(['#!/user/bin/sh\n',
                             'exec tail -n +3 $0\n\n',
                             'menuentry "CentOS Stream 9 Installer" {\n',
                             '\tset root=(hd1)\n',
                             '\tdrivemap -s hd0 hd1\n',
                             '\tchainloader +1\n',
                             '}'
                             ]))
    menuentry.close()

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
    print('Warning: Use this script at your own risk.\n')

    # Ask for confirmation
    confirm = input('Continue? [y/N] ')
    if confirm.lower() != 'y':
        print('Exiting...')
        exit(0)

    # Ask to skip downloading the ISO
    skip_download = input('Skip downloading the ISO? [y/N] ')
    if skip_download.lower() != 'y':
        download_iso()
    else:
        print('\nSkipping download...')
        print(f'Please ensure the ISO is located at /tmp/{CENTOS_ISO}.')
        input('Press Enter to continue...')

    # Configure the ISO for booting
    unpack_iso()
    add_boot_option()

    # Reboot
    input('Press Enter to reboot...')
    call('reboot', shell=True)


# Only if this file is run directly
if __name__ == '__main__':
    main()
