# Reset CentOS Linux 7 to CentOS Stream 9

## 1. During Deployment (Recommended)

> **Note**\
> This doesn't seem to be an option for the CentOS7_netB machines.

1. When requesting the NSSA 245 deployment navigate to the "CentOS7" Machine.
2. On the "General" tab, set memory to `4096` or the maximum value possible.
3. Edit the description as you see fit, reconfiguration is not possible later.
4. Navigate to the "Storage" tab.
5. Select the **➕ New** button, set the capacity to `12`GB and the label to `Image`, and then select **Ok**.
6. Select **SUBMIT** in the bottom left to start deployment.

## 1. Create Partition

### Resize CentOS Home Volume

1. Log out of the **student** account and login as *root*.
   To do this click **Not Listed?** on the home screen.
1. XFS file systems cannot be shrunk, therefore we need to wipe and reconfigure the `centos-home` volume.
1. Open a Terminal and backup the `/home` contents.
   ```shell
   tar -czvf /root/home.tgz -C /home .
   ```
1. Test the backup of the home directory.
   ```shell
   tar -tvf /root/home.tgz
   ```
1. Unmount `/home`.
   ```shell
   umount /dev/mapper/centos-home
   ```
1. Remove the `/home` logical volume.
   ```shell
   lvremove /dev/mapper/centos-home
   ```
1. Recreate the `/home` logical volume with a size of `38GB`, this leaves ~12 for the partition we will be making later.
   ```shell
   lvcreate -L 38GB -n home centos
   ```
1. Format and mount the new `/home` volume.
   ```shell
   mkfs.xfs /dev/centos/home
   mount /dev/mapper/centos-home
   ```
1. Restore the backup of `/home`.
   ```shell
   tar -xzvf /root/home.tgz -C /home
   ```
1. Reset security context of the `/home` contents using `restorecon`
   ```shell
   restorecon -R -v /home
   ```
1. Log out of the **root** user and sign back in as **student**.
1. Now that we have verified that the **student** account is working again we can delete the backup.
   ```shell
   sudo rm /root/home.tgz
   ```
### Add New Volume




## 2. Connect CentOS Linux 7 to Network

1. First identify what side of the Pfsense Router your machine is attached to. Either NetA or NetB.
1. Open the Wired Network settings and set the IPV4 method to **Manual**.
1. Set the Address to `10.x.255.yyy`, the Netmask to `255.255.0.0`, and the Gateway to `10.x.255.254`.
   `x` being `1` for NetA and `2` for NetB, you can choose `yyy` but don't use the same value for every machine.
1. Set the DNS to `1.1.1.1` and turn off Automatic DNS.
1. Refresh the Wired Network by rebooting the machine.
   This seems to produce better results that simply turning the Wired connection on and off.

## 3. Update CentOS Linux 7 (Optional)

1. Open a Terminal in CentOS 7 and clean the yum cache.
    ```shell
    sudo yum clean all
    ```
1. Update all packages using yum.
   If the yum repos can't be resolved then reboot the machine and start over at step 1.
   ```shell
   sudo yum upgrade -y
   ```
1. Wait for CentOS to upgrade all packages and then reboot the machine.
   ```shell
    reboot
   ```
1. It is recommended, but not required, to clean the yum cache again.
   ```shell
    sudo yum clean all
   ```

## 4. Download CentOS Stream 9 ISO

1. Open Firefox and then go to [`https://centos.org/download/`](https://centos.org/download/).
1. Select **CentOS Stream**, then select **9**, and then select **x86_64**.
   Alternatively you can [select or go to this download link](https://mirrors.centos.org/mirrorlist?path=/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso&redirect=1&protocol=https) on the machine.
1. Save the file to your downloads.

## 5. Prepare the CentOS 9 ISO for booting

We need to unpack the CentOS Stream 9 ISO onto the "Image" drive we created during deployment.
We can then boot from the "Image" drive and install CentOS Stream 9 in the place of CentOS 7.

1. First we need to mount and prepare the empty drive.
   ```shell
   sudo fdisk -l
   ```
1. Find the ~`12`GB Disk we created during deployment, most likely labelled as `/dev/sdc`.
1. Format the new drive using the correct label such as `/dev/sdc`.
```shell
sudo mkfs -t ext4 /dev/sdc
```
1. Unpack the CentOS Stream 9 ISO onto the new drive.
   Make sure to set `if=` to the path of the ISO and `of=` to the correct drive.
   ```shell
   sudo dd if=/home/student/Downloads/CentOS-Stream-9-latest-x86_64-dvd1.iso of=/dev/sdc bs=512k status=progress
   ```
   
## 6. Add the CentOS Stream 9 Bootable Disk to the Grub Menu

```shell
sudo vim /etc/grub.d/40_custom
```
```shell
menuentry "CentOS Stream 9 Installer" {
  set root=(hd2)
  drivemap -s hd0 hd2
  chainloader +1
}
```
```shell
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
```shell
reboot
```
1. Select **CentOS Stream 9 Installer** during boot.

### 7. Install CentOS Stream 9

1. 


