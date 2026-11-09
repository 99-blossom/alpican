# Installation (fastboot)

> [!CAUTION]
> **PLEASE READ THIS ENTIRE GUIDE SLOWLY, CAREFULLY, AND FROM BEGINNING TO END!! MAKE SURE YOU FULLY UNDERSTAND EVERY STEP, NOTE, AND INSTRUCTION BEFORE YOU START!! DO NOT SKIP ANY PART OF THIS GUIDE, AS DOING SO MAY LEAD TO ERRORS OR UNEXPECTED PROBLEMS LATER!!**

> [!WARNING]
> * **Back up all important data** from your device before proceeding.
> * **Make sure you have recovery tools** (such as SP Flash Tool or `mtkclient`) and a stock firmware image in case of a hard brick.

## Partition Backup

The installer overwrites the `boot`, `vbmeta`, `lk`, and `logo` partitions, and also `userdata` unless you skip flashing it (see the userdata question in [Installation](#installation)). Back up the partitions in advance from Android with root access:

```sh
dd if=/dev/block/by-name/boot of=/sdcard/boot.img
dd if=/dev/block/by-name/lk of=/sdcard/lk.img
dd if=/dev/block/by-name/logo of=/sdcard/logo.bin
dd if=/dev/block/by-name/vbmeta of=/sdcard/vbmeta.img

dd if=/dev/block/by-name/nvdata of=/sdcard/nvdata.bin
dd if=/dev/block/by-name/nvcfg of=/sdcard/nvcfg.bin
dd if=/dev/block/by-name/nvram of=/sdcard/nvram.bin
```

> `if=` is the input file (where to read from), and `of=` is the output file (where to save to). Swapping them overwrites the partition, so double-check the syntax.

> [!NOTE]
> The installer does not touch `nvdata`, `nvcfg`, or `nvram`. Keep copies of them anyway: the `nvdata`, `nvcfg`, and `nvram` partitions store your IMEI.

> [!CAUTION]
> The backups above **do not include** `userdata` (personal files, apps, photos). If you choose to flash `userdata` (answer `n` to "Skip flashing userdata partition?"), this partition will be **completely erased**. To keep your data, copy what you need in advance (via `adb pull`, MTP, or cloud storage) **before** running the installer.

You can copy the files to your computer over ADB:

```sh
adb pull /sdcard/boot.img ./
adb pull /sdcard/lk.img ./
adb pull /sdcard/lk2.img ./
adb pull /sdcard/logo.bin ./
adb pull /sdcard/vbmeta.img ./

adb pull /sdcard/nvdata.bin ./
adb pull /sdcard/nvcfg.bin ./
adb pull /sdcard/nvram.bin ./
```

## Preparation

1. Install MIUI 12.5 on the phone. Take the stock `boot.img` (see [Installation](#installation)) from the same firmware.

2. Install `adb` and `fastboot` on your computer:

   ```sh
   pacman -S android-tools                      # arch / arch-based
   emerge dev-util/android-tools                # gentoo / gentoo-based
   apt install adb fastboot                     # debian / debian-based
   brew install --cask android-platform-tools   # macOS

   # on other distributions, look for packages named android-tools, adb, or fastboot
   ```

   Or download platform-tools from [developer.android.com](https://developer.android.com/tools/releases/platform-tools#downloads).

3. Check the versions:

   ```sh
   fastboot --version
   adb --version
   ```

4. Make sure your user is in the `plugdev` group:

   ```sh
   groups
   ```

   If the group is missing, add your user to it and log in again:

   ```sh
   usermod -aG plugdev $USER
   ```

5. Charge the phone to at least 25%.

## Installation

### Get the archive

Download the latest archive from the [**Releases**](https://github.com/99-blossom/alpican/releases/latest) page and extract it.


### Place the stock boot.img

Copy the stock `boot.img` into the `alpican/` directory and rename it to `boot-stock.img`. The file must sit next to `install.sh`, not in `images/`:

```
alpican/
├── bin/
├── boot-stock.img   ← stock boot.img
├── images/
├── kernel/
├── install.bat
└── install.sh
```

Without this file, the installer exits with an error.
> [!NOTE]
> The DTB from your stock `boot.img` is kept in the image together with the new kernel. Therefore, `boot-stock.img` must be taken from your own phone, from the same firmware that is installed on it. An image from a different firmware or a different model may fail to boot.

### Connect the phone in fastboot mode

1. Put the phone into fastboot mode and connect it to your computer.
2. Check that the computer detects the device:

   ```sh
   fastboot devices
   ```

   The output should look like this:

   ```sh
   1234567890ABCBD         fastboot
   ```

### Run the installer

Run the script **from inside the `alpican/` directory**:

Linux / macOS:

```sh
cd alpican
./install.sh
```

If you get `Permission denied`, make the script executable and run it again:

```sh
chmod +x install.sh
./install.sh
```

Windows (cmd, from the `alpican\` directory):

```bat
install.bat
```

> [!IMPORTANT]
> Windows: the installer supports x86-64 only. Installation from ARM64 Windows is not supported.

### Installer questions

The installer asks the following questions in order. Any input other than the valid options aborts the installation.

1. **Are you ready? [y/N]** - enter `y` to continue.

2. **Which LK?** - choose the bootloader image:
   * `1` - `lk_blossom_R.img`: custom boot logo support.
   * `2` - `oem-cdms-logo-lk.img`: custom boot logo support and a fix for the `dm-verity corruption` error.

   > [!NOTE]
   >
   > If `oem-cdms-logo-lk.img` is selected, the host identifier may be displayed as **MT6762G**. This is expected behavior and does not affect system functionality.
   >
   > [This happens because this LK comes from the Redmi 10A firmware (MIUI 12.5.4.0 RCZCNXM) and uses the platform identifier MT6762G rather than the device codename.](https://4pda.to/forum/index.php?act=findpost&pid=139550809&anchor=Spoil-139550809-2)

3. **Which logo?** - choose the boot logo:
   * `1` - `logo_redmi_alpine.bin`: the standard Redmi logo with **Powered by Alpine** instead of **Android**.
   * `2` - do not flash the `logo` partition. Choose this if the current logo is fine for you.

4. **Skip flashing userdata partition? [y/N]** - the answer depends on the type of installation:
   * `n` - standard installation: `rootfs.img` is written to `userdata`, and all data will be erased.
   * `y` - skip `userdata`.

When the installation finishes, reboot the phone:

```sh
fastboot reboot
```

> [!TIP]
> If you flashed `rootfs.img` to `userdata` and the system only sees ~500 MB (the original image size), expand the filesystem to fill the whole partition:
>
> ```sh
> resize2fs /dev/mmcblk0p41
> ```
>
> `resize2fs` is bundled in the rootfs by default starting with version 5.0.

## Passwords

* **root:** `1`