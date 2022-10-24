# Reset CentOS Linux 7 to CentOS Stream 9

## 0. Update CentOS Linux 7 (Optional)

1. Open a Terminal instance and clean the yum cache.
    ```shell
    sudo yum clean all
    ```
2. Using the yum package manager, upgrade all packages.
   *If the yum repos can't be resolved then reboot and start over at step 1.*
   ```shell
   sudo yum upgrade -y
   ```
3. Once complete it is recommended, but not required, to clean the yum cache again.
   ```shell
    sudo yum clean all
   ```
4. Finally, reboot the machine.
   ```shell
    reboot
   ```
   
## 0. Script

> **Warning**\
> This script can damage your system.
> This script will overwrite /dev/sdb.
> This script is provided as-is and is not supported by the CentOS Project.
> Use at your own risk.

Running the `install-centos.py` script will perform steps 1-3 automatically.

1. Install `git` and `python3`.
    ```shell
    sudo yum install -y git python3
    ```
2. Clone this repository.
    ```shell
    git clone https://github.com/aisgbnok/NSSA245-Notes.git
    ```
3. Run the `install-centos.py` script.
    ```shell
    cd NSSA245-Notes/scripts/
    sudo python3 install-centos.py
    ```
4. Skip to step [4. Install CentOS Stream 9](#4-install-centos-stream-9).

## 1. Download CentOS Stream 9 ISO

1. Open a browser and then go to [`https://centos.org/download/`](https://centos.org/download/).
   *If the URL fails to resolve then reboot and try again.*
2. Select **CentOS Stream**, select **9**, and then select **x86_64**.
   Alternatively you can [select or go to this download link](https://mirrors.centos.org/mirrorlist?path=/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso&redirect=1&protocol=https) on the machine.
3. Save the file to your downloads directory.

## 2. Prepare the CentOS 9 ISO for booting

We need to unpack the CentOS Stream 9 ISO onto the "Installer" drive we created during deployment.
We can then boot from the "Installer" drive and install CentOS Stream 9 in the place of CentOS 7.
*This will completely wipe CentOS Linux 7.*

1. Use the `fdisk` program to list all partition tables.
   ```shell
   sudo fdisk -l
   ```
2. Find the `/dev/sdb` Disk, it should be about `12.9`GB in size.
   This is the `Installer` drive we added during deployment.
3. Unpack the CentOS Stream 9 ISO onto the new drive.
   Make sure to set `if=` to the path of the ISO and `of=` to the correct drive.
   ```shell
   sudo dd if=/home/student/Downloads/CentOS-Stream-9-latest-x86_64-dvd1.iso of=/dev/sdb bs=512k status=progress
   ```

## 3. Add the CentOS Stream 9 Bootable Disk to the Grub2 Menu

1. Create a custom grub menu entry.
   We will create a `40_custom` file to do this.
   ```shell
   sudo vim /etc/grub.d/40_custom
   ```
2. Press <kbd>i</kbd> and <kbd>CTRL</kbd>+<kbd>END</kbd> to navigate to the end of the file.
3. Enter two spaces, leaving a single empty space between the last comment.
4. Enter the following.
   ```text
   menuentry "CentOS Stream 9 Installer" {
     set root=(hd1)
     drivemap -s hd0 hd1
     chainloader +1
   }
   ```
5. Save and exit the file. <kbd>ESC</kbd><kbd>:</kbd><kbd>w</kbd><kbd>q</kbd><kbd>ENTER</kbd>
6. Rebuild the grub2 menu.
   ```shell
   sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```
7. Reboot the machine.
   ```shell
   reboot
   ```

## 4. Install CentOS Stream 9

1. During boot, select the **CentOS Stream 9 Installer** entry we just created.
2. Select **Install CentOS Stream 9**.
3. Choose your language and then select **Continue**.
4. Select **Installation Destination** and then select **Done** in the top left corner.
5. Select **Reclaim space**, select **Delete all**, and then select **Reclaim space**.
6. Select **Root Password** and then choose a root password, select **Done** when satisfied.
   *Security is not an important factor for these labs, so I chose `student` as the password.*
7. Select **Begin Installation** to start the installation process.
8. Once complete, select **Reboot System**.

## 5. Setup CentOS Stream 9

1. Select **Start Setup**, disable Location Services, select **Next**, then select **Skip**.
2. Use the Full Name you entered into the description during deployment.
   I chose `Student`. Select **Next**.
3. Similarly, use the Password you chose. I chose `student`. Select **Next**.
4. Select **Start Using CentOS Stream**.
