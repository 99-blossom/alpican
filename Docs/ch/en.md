## 3.0 (Latest)
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