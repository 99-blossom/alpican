# Installation

## Preparation:

1.  Install MIUI 12.5 on the phone.

2.  Install ADB and Fastboot on the host machine:

``` sh
pacman -S android-tools # arch/arch based
emerge dev-util/android-tools # gentoo
apt install adb fastboot # debian/debian based
# ... on other distributions look for packages like `android-tools`, `adb`, `fastboot`
```

3.  Check versions:

``` sh
fastboot --version
adb --version
```

4.  Ensure your user is in the `plugdev` group:

``` sh
groups
```

If not, add the user to this group and re-login:

``` sh
usermod -aG plugdev $USER
```

5.  Ensure the device is at least 25% charged.

## Installation

Download the archive from [this](https://drive.google.com/file/d/1Kr9nITzsnQoedxKQAV0Lj__joKi8Ze6M/view?usp=sharing) link.

Extract the ROM archive. Inside should be: `boot.img`, `logo.bin`,
`rootfs.img`, `vbmeta.img`, `lk_blossom_R.img`, and the installer script
`install.sh`.

1.  Connect the device to the computer in `fastboot` mode. Check if the
    computer detects it:

``` sh
fastboot devices
```

The output should look like:

``` sh
1234567890ABCBD         fastboot
```

2.  Run the installation script:

``` sh
./install.sh
```

If you get `Permission denied`, make the script executable and run it
again:

``` sh
chmod +x install.sh
./install.sh
```

3.  Follow the instructions inside the script.

## Passwords
* root : 1
