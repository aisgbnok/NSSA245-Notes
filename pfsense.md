# pfSense Setup

## Setup Web GUI

1. Choose a client device (Windows or Linux) to connect to pfSense through the Web GUI.
2. Identify whether your client is connected to NetA or NetB.
3. Manually configure your IPv4 address to `10.x.255.yyy` with a `/16` netmask and a gateway of `10.x.255.254`.
   `x` being `1` for NetA and `2` for NetB, you can choose `yyy`.
4. Optionally set your DNS to `1.1.1.1` and `1.0.0.1`.
5. In a browser go to 10.x.255.254 and login.
   Username: `admin`.
   Password: `pfsense`.

## Update pfSense

1. In the pfSense Web GUI navigate to **System** > **Update**.
2. Change the **Branch** to the **Previous stable version**, then select **Confirm**.
3. Once pfSense has rebooted log back into the Web GUI.
4. This time update to the **Latest stable version**.
5. Once pfSense has rebooted log back into the Web GUI.
6. Ensure you are on the latest version of pfSense.
   `2.6.0` at the time of writing.

## Factory Reset pfSense
1. Log into the pfSense Web GUI.
2. Navigate to **Diagnostics** > **Factory Defaults**, then select **Factory Reset**.
3. This will take approximately 1 minute to complete.

> **Note**\
> The network addresses will be changed during reset.
> Therefore, your client device will no longer be able to access the Web GUI.
> You do not need to fix this yet.

## Configure pfSense

### Assign Interfaces

1. Enter <kbd>1</kbd> to select option **1) Assign Interfaces**.
2. Do not setup VLANs. <kbd>n</kbd>
3. Enter <kbd>em0</kbd> for the **WAN** interface.
4. Enter <kbd>em1</kbd> for the **LAN** interface.
5. Enter <kbd>em2</kbd> for the **Optional 1** interface.
6. Confirm your choices. <kbd>y</kbd>

### Assign IP Addresses

1. Enter <kbd>2</kbd> to select option **2) Set interface(s) IP address**.
2. Enter <kbd>2</kbd> to configure **em1**, which is **Network A**.
3. Choose the router's IPv4 address, such as <kbd>10.150.84.254</kbd>.
4. Set the IPv4 subnet bit count to <kbd>24</kbd>.
5. For the upstream gateway and the IPv6 address press <kbd>Enter</kbd> for none.
6. Enable the DHCP server. <kbd>y</kbd>
7. Choose the start address range, such as <kbd>10.150.84.10</kbd>.
8. Choose the end address range, such as <kbd>10.150.84.100</kbd>.
9. Do not revert to HTTP. <kbd>n</kbd>
10. Once finished press <kbd>Enter</kbd>.

Repeat for **Network B** with the following modifications:

- For step 2, enter <kbd>3</kbd> to configure **em2**, which is **Network B**.
- Choose a different network address.
  For example if you used `10.150.84.254`, replace the `84` with `85`.
  Do the same when setting the DHCP ranges.

### pfSense Setup Wizard

1. Set your client device to automatically obtain an IPv4 address.
2. In a browser go to the router's IPv4 address you chose in step 3.
3. Log into the pfSense Web GUI.
4. Step through the Setup Wizard until you get to **General Information**.
5. Set the **Domain** to your RIT ID such as `abc1234.rit`.
6. Optionally set the DNS servers to `1.1.1.1` and `1.0.0.1`.
7. Step through the Setup Wizard until you get to **WebGUI Password**.
8. Set the password to what you chose to put in the RLES **pfSense** description.
9. Reload pfSense and then select **Finish** to go to the Dashboard.

### Finish pfSense Configuration

#### Network Names

1. In the pfSense Web GUI navigate to **Interfaces** > **LAN**.
2. Set the **Description** to **NetA**, select **Save**.
3. Repeat for **OPT1**, setting a **Description** of **NetB**.

#### Network B Firewall

1. In the pfSense Web GUI navigate to **Firewall** > **Rules** > **NETA**.
2. Select the **Copy** button for the description **Default allow LAN to any rule**.
3. Replace **NETA** with **NETB** for **Interface** and **Source**, then select **Save**.
4. Optionally repeat the process for the IPv6 rule.
5. Select **Apply Changes** to reload the firewall.
6. Once complete Network B should now have internet access.

## Restart pfSense

Once all of this has been completed it is recommended to restart pfSense.
This can be done in the Web GUI (**Diagnostics** > **Reboot**) or from the console (Enter <kbd>5</kbd> to select option **5) Reboot system**).