# Reset Windows

## Windows Client

### Windows 11 Bypass

If you choose to install Windows 11, then you need to bypass the requirements.
*You can skip this section if you are not installing Windows 11.*

1. Download and run AveYo's [`Windows11Bypass.cmd`](/scripts/Windows11Bypass.cmd) script.

*Credit goes to [AveYo](https://github.com/AveYo/MediaCreationTool.bat/blob/979fd14f21a4e72c1599c0296a94dbd2fcc184ed/bypass11/Skip_TPM_Check_on_Dynamic_Update.cmd) for the script.*

### Install Windows Enterprise

1. Download the latest Windows Enterprise ISO from your Azure Portal or build one using [UUP dump](https://uupdump.net/).
   *If you are a student at RIT I can provide a link to an ISO upon request.* 
2. Mount the Windows ISO and then run `setup.exe`.
3. Once Windows Setup loads, select **Next**.
4. **Accept** the applicable notices and license terms.
5. Choose to keep **Nothing** and then select **Next**.
6. Ensure that **Windows Enterprise** will be installed and that it will **Keep nothing**, then select **Install**.

### Setup Windows Enterprise

1. Step through the Windows Out of Box Experience (OOBE) until you get to account creation.
2. Select **Sign-in options** and then select **Domain join instead**.
3. Use the username and password you entered into the description during deployment.
   I chose `Student` as the username and `student` as the password.
4. Fill out the security questions.
   I chose the first three questions and set all answers to `student`.
5. Turn off all telemetry or "privacy" settings.
6. Select **Accept**, if you are prompted for Cortana select **Not now**.

### Install VMWare Tools

1. Download the latest VMware tools for Windows.
   *If you are a student at RIT I can provide a link upon request.*
2. Run the VMware tools installer.
3. Select **Next**, choose **Complete**, select **Next**, and then select **Install**.
4. It is recommended to restart your system, select **Yes**.

## Windows Server

### Install Windows Server

> **Warning**\
> Check [Microsoft's Windows Server upgrades](https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview#which-version-of-windows-server-should-i-upgrade-to) article to see the latest compatible version you can upgrade to.
> For example, Windows Server 2012 R2 must upgrade to 2019 before upgrading to 2022.

1. Download the latest compatible Windows Server ISO from your Azure Portal or build one using [UUP dump](https://uupdump.net/).
   *If you are a student at RIT I can provide a link to an ISO upon request.*
2. Mount the Windows ISO and then run `setup.exe`.
3. Once Windows Setup loads, select **Change how Setup downloads updates**.
4. Choose **Not right now** to disable downloading updates, then select **Next**.
5. Enter the product key provided in your Azure Portal, then select **Next**.
6. Choose **Windows Server Datacenter (Desktop Experience)**, then select **Next**.
7. **Accept** the applicable notices and license terms.
8. Choose to keep **Nothing** and then select **Next**.
9. Ensure that **Windows Server Datacenter** will be installed and that it will **Keep nothing**, then select **Install**.
10. Once complete, repeat this process until you are on the latest Windows Server version.

> **Warning**\
> If you run into a `SAFE_OS` error on Windows Server 2012 R2, then you need to use an ISO with an earlier build of Windows Server 2022 such as build `20348.169`.

> **Note**\
> You will have to download a modern browser to replace Internet Explorer on Windows Server 2019 and earlier.

### Setup Windows Server

1. Choose your region, language, and keyboard layout, then select **Next**.
2. Use the password you entered into the description during deployment.
   I chose `Student123` as the password.
3. Log in.
4. When you desktop loads, wait for the Networks side panel to appear.
5. Select **Yes** for allowing your PC to be discoverable.

### Time Server

1. Open **Windows Settings** > **Time & Language** > **Date & Time**.
2. Choose the appropriate time zone and then select **Sync now**.
3. 
