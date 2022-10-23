# Reset Windows

###

1. Google Chrome
2. Mozilla Firefox
3. PuTTY
4. VMware Tools
5. Wireshark
   6. Npcap
   7. WinPcap

## Windows Client

### Windows 11 Bypass

If you choose to install Windows 11, then you need to bypass the requirements.
*You can skip this section if you are not installing Windows 11.*

1. Download and run AveYo's [Windows11Bypass.cmd](/configs/Windows11Bypass.cmd) found in the `configs` directory.

*Credit goes to [AveYo](https://github.com/AveYo/MediaCreationTool.bat/blob/979fd14f21a4e72c1599c0296a94dbd2fcc184ed/bypass11/Skip_TPM_Check_on_Dynamic_Update.cmd) for the script.*

### Install Windows

1. Download the latest Windows Enterprise ISO from your Azure Portal or build one using [UUP dump](https://uupdump.net/).
   *If you are a student at RIT I can provide a link to an ISO upon request.* 
1. Mount the Windows ISO and then run `setup.exe`.
2. Once Windows Setup loads, select **Next**.
3. Select **Accept** for the notices and license terms.
4. Choose to keep **Nothing** and then select **Next**.
5. Ensure that **Windows Enterprise** will be installed and that it will **Keep nothing**, then select **Install**.
