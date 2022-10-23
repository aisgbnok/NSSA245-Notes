# Reset Windows

## Windows Client

### Windows 11 Bypass

If you choose to install Windows 11, then you need to bypass the requirements.
*You can skip this section if you are not installing Windows 11.*

1. Download and run AveYo's [`Windows11Bypass.cmd`](/scripts/Windows11Bypass.cmd) script.

*Credit goes to [AveYo](https://github.com/AveYo/MediaCreationTool.bat/blob/979fd14f21a4e72c1599c0296a94dbd2fcc184ed/bypass11/Skip_TPM_Check_on_Dynamic_Update.cmd) for the script.*

### Install Windows

1. Download the latest Windows Enterprise ISO from your Azure Portal or build one using [UUP dump](https://uupdump.net/).
   *If you are a student at RIT I can provide a link to an ISO upon request.* 
2. Mount the Windows ISO and then run `setup.exe`.
3. Once Windows Setup loads, select **Next**.
4. **Accept** the applicable notices and license terms.
5. Choose to keep **Nothing** and then select **Next**.
6. Ensure that **Windows Enterprise** will be installed and that it will **Keep nothing**, then select **Install**.

### Setup Windows

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
