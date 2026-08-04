## 4.1 (Latest)
* **initramfs**:
  - Fixed a typo in stream redirection (`2>&0` replaced with `2>&1`) for proper error logging in the emergency shell over ACM,
  - Dynamic device parsing from `androidboot.hwname=`, replacing hardcoded **Redmi 9C NFC**,
* **install.sh**: 
  - Added an option to skip flashing `logo.bin`,
* **rootfs**: 
  - Fixed `sshd` status display overlapping `agetty`,
* **Misc**:
  - Switched from Google Drive to [GitHub Releases](https://github.com/99-blossom/alpican/releases) for hosting release files

## 4.0
* **Kernel**:
  - Added `systemd` support (enabled `FHANDLE`, `AUTOFS`, `AUDIT`, `CRYPTO_USER_API_HASH`, `CRYPTO_HMAC`),
  - Stripped unused initramfs decompressors (`LZ4`, `LZO`, `bzip2`, `LZMA`, `XZ`, `zstd`),
  - Disabled `CONFIG_DEBUG_INFO`.
  - Removed the `-st8` version suffix,
  - Removed the `logo.nologo` parameter from **cmdline**,
  - Removed the `buildvariant=userdebug` parameter from cmdline,
  - Removed duplicate call to `info->fbops->fb_imageblit(info, image);` in `bitblit.c`
  - Replaced `dbg_fb_*` **debug** functions with `cfb_fillrect` and `cfb_imageblit`
* **rootfs**
  - Fixed WiFi startup race condition (merged `mtk-wifi` and `wmt-pyloader` services),
  -  Added the **`vibro`** command to `twc`,
* **USB Gadget**: Device serial number is now written to the configuration,
* **initramfs**:
  - Added ACM serial console initialization status output during boot,
  - Added dynamic parsing of the root partition from `cmdline` parameters (selecting the last `root=` parameter specified, ignoring `root=/dev/ram*` parameters and displaying a warning) instead of hardcoding `/dev/mmcblk0p41`,
  - Increased root device timeout (`root_timeout`) from 15 to 25 seconds.
* **install.sh**:
  - Refactored user interaction (UX improvements),
  - Added `--skip-device-verification` flag,
  - `fastboot reboot bootloader` is now executed before `oem cdms`, without which `oem cdms` would not work.

## 3.0
* **install.sh**: 
  - Added LK image selection (`lk_blossom_R.img` / `oem-cdms-logo-lk.img`),
  - Refactored user interaction (UX improvements),
* **initramfs**:
  - Improved error handling,
  - Fixed root device race condition,
  - Upgraded BusyBox to v1.36.1 (static aarch64),
* **USB Gadget**: Configured USB `ConfigFS` with ACM serial console function in initramfs and rootfs for emergency debugging, etc. (115200),
* **Battery**: Fixed charging status and battery level percentage display (switched to kernel-side hardware Coulomb counter and corrected voltage scaling),
* **fbcon**: Fixed cursor visibility (`cur 2`),
* **Dynamic AIK build**: `boot.img` size now scales with kernel and initramfs, resulting in up to 4× faster `fastboot flash`,
* **Utility rename**: (`tc` **→** `twc`) to avoid conflict with Linux Traffic Control,
* **vbmeta**: Switched to an empty `vbmeta.img` instead of stock MIUI 12.5 `vbmeta.img`,

## 2.0
* Kernel upgrade (`4.19.275-angentoo-kyae` **→** `4.19.325-st8-gnulinux-unified`),
* Touchscreen fixes (integrated firmware binaries into `initramfs /lib/firmware`),
* New `tc` utility (flashlight control, LCD brightness control, etc.),
* `btop` is now bundled by default,
* `ssh` (`openssh`) is now bundled by default (PermitRootLogin yes),
* Fixed a typo in `initramfs`,

## 1.0
* Initial build.