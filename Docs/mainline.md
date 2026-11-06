## Mainline / U-Boot
[← Back to README](../README.md)

### U-Boot
Previously, U-Boot was chain-loaded by LK. Now it boots **instead of** LK, using [this fork](https://github.com/knukima/u-boot-mt6765):

<img src="../assets/u-boot-lk.jpg" alt="U-Boot booting instead of LK" width="500">

<br>
However, I have no plans to replace LK with U-Boot at the moment.

### Mainline Kernel
Alpican can boot into Alpine userspace from an SD card on mainline kernel 7.1.0 using [uniLoader](https://github.com/ivoszbg/uniLoader), which officially supports `xiaomi-blossom` :

<img src="../assets/mainline-7.1.0.jpg" alt="Alpican running mainline kernel 7.1.0" width="400">


### pmOS moment
<p>
<img src="../assets/pmos_moment.png" alt="pmos moment" width="400">
</p>