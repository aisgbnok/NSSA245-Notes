# Request Deployment

1. Go to the RLES **Catalog** tab, find the **NSSA-245-VMs** deployment, and then select **REQUEST**.
1. Go through and configure all machines.
   Below is a table with suggested memory and description values.
   I would recommend setting the **Memory** value to the maximum possible value, as long as it isn't excessive.
   Chose descriptions that list the OS versions and passwords you will be using.
   If you continue following this guide we will be resetting all machines except for **CentOS7_netB**, keep that in mind when setting your descriptions.
   
   > **Warning**\
   > Unfortunately this deployment cannot be reconfigured after provisioning.
   > Therefore, make sure you are satisfied with your configurations and descriptions as they cannot be changed once submitted.
 
   |                   Name | Memory (MB) | Description                                   | Reset |
   |-----------------------:|:-----------:|:----------------------------------------------|:-----:|
   |            **pfSense** |   `1024`    | admin/pfsense                                 | True  |
   |       **CentOS7_netA** |   `4096`    | CentOS Stream 9; Student/student              | True  |
   |         **Win10_netA** |             | Windows 11 22H2; Student/student              | True  |
   |   **WinServ2016_netA** |             | Windows Server 2022; Administrator/Student123 | True  |
   | **WinServ2012R2_netA** |             | Windows Server 2022; Administrator/Student123 | True  |
   |       **CentOS7_netB** |   `4096`    | CentOS Linux 7; student/student               | False |
   |         **Win10_netB** |             | Windows 11 22H2; Student/student              | True  |
   |   **WinServ2016_netB** |             | Windows Server 2022; Administrator/Student123 | True  |
   | **WinServ2012R2_netB** |   `4096`    | Windows Server 2022; Administrator/Student123 | True  |

1. Once you have configured all machines to your liking, select the **CentOS7_netA** machine.
1. Select the **Storage** tab, then select the **➕ New** button.
   Set **Capacity (GB)** to `12`, **Label** to `Installer`, and then select **Ok**.
1. Select **SUBMIT** in the bottom left to finalize the deployment.
   *It may take several minutes for the deployment to provision.*