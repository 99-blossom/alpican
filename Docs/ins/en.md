# Installation

## Preparation:

> [!CAUTION]
> **PLEASE READ THIS ENTIRE GUIDE SLOWLY, CAREFULLY, AND FROM BEGINNING TO END!! MAKE SURE YOU FULLY UNDERSTAND EVERY STEP, NOTE, AND INSTRUCTION BEFORE YOU START!! DO NOT SKIP ANY PART OF THIS GUIDE, AS DOING SO MAY LEAD TO ERRORS OR UNEXPECTED PROBLEMS LATER!!**

> [!WARNING]
> * **Back up all important data** from your device before proceeding.
> * **Ensure you have access to unbricking tools** (such as SP Flash Tool or `mtkclient`) and have a stock firmware image ready in case of a hard brick.

1. Install MIUI 12.5 on the phone.

2. Install ADB and Fastboot on the host machine:
   ```sh
   pacman -S android-tools # arch/arch based
   emerge dev-util/android-tools # gentoo
   apt install adb fastboot # debian/debian based
   # ... on other distributions look for packages like `android-tools`, `adb`, `fastboot`
   ```

3. Check versions:
   ```sh
   fastboot --version
   adb --version
   ```

4. Ensure your user is in the `plugdev` group:
   ```sh
   groups
   ```
   If not, add the user to this group and re-login:
   ```sh
   usermod -aG plugdev $USER
   ```

5. Ensure the device is at least 25% charged.

## Installation

Download the archive from [this](https://drive.google.com/file/d/1Tf3dM5eRfAEaKKZisNR0pVCe43HCSaTp/view?usp=sharing) link.

Extract the ROM archive. Inside should be: `boot.img`, `logo.bin`, `rootfs.img`, `vbmeta.img`, `oem-cdms-logo-lk.img`, `lk_blossom_R.img`, and the installer script `install.sh`.

1. Connect the device to the computer in `fastboot` mode. Check if the computer detects it:
   ```sh
   fastboot devices
   ```
   The output should look like:
   ```sh
   1234567890ABCBD         fastboot
   ```

2. Run the installation script:
   ```sh
   ./install.sh
   ```
   If you get `Permission denied`, make the script executable and run it again:
   ```sh
   chmod +x install.sh
   ./install.sh
   ```

3. Follow the instructions inside the script.

> [!NOTE]
> If `oem-cdms-logo-lk.img` is selected, the host identifier may be displayed as **MT6762G**. This is expected behavior and does not affect system functionality.
>
> [This occurs because this LK is based on the Redmi 10A firmware (MIUI 12.5.4.0 RCZCNXM) and uses the platform identifier MT6762G rather than the device codename.](https://4pda.to/forum/index.php?act=findpost&pid=139550809&anchor=Spoil-139550809-2)

> [!TIP]
> If you flashed `rootfs.img` to `userdata` and the system only sees ~500 MB of space (the original image size), expand the filesystem to fill the entire partition using `resize2fs` from the `e2fsprogs-extra` package:
> ```sh
> apk add e2fsprogs-extra
> resize2fs /dev/mmcblk0p41
> ```

## Passwords
* root : 1
