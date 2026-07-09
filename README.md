<br>
<p align="center">
  <img src="https://www.alpinelinux.org/alpinelinux-logo.svg" width="300"/>
</p>
<h2 align="center">Alpican (11 / R)</h2>
<p align="center">Alpine Linux port for Redmi 9C NFC: Again.</p>

> [!WARNING]  
> I am **NOT** responsible for **any** damage to your device, including but **NOT** limited to bricking, hardware failure, software malfunction, data loss, security issues, loss of warranty, or **any** other negative consequences that _may_ occur. **You are solely responsible** for any actions you take and any modifications you apply.
>
> Proceed **only** if you fully understand what you are doing and accept all associated risks. If not, please leave this page!

## Changelog
* **Alpican version:** v3.0 (based on Alpine v3.24, aarch64);
* [🇬🇧 Changelog EN](Docs/ch/en.md)
* [🇷🇺 Changelog RU](Docs/ch/ru.md)

## Images
<img src="assets/ssh.png" alt="ssh"><img src="assets/2.jpg" width=300 alt="2"> <img src="assets/3.jpg" width=300 alt="3"> <img src="assets/4.jpg" width=300 alt="4"> <img src="assets/6.jpg" width=300 alt="6">

[all screenshots](Docs/allimg/un.md)

## Why
This project **aims** to bring a minimal, fast, and highly customizable `Alpine Linux` environment to the Redmi 9C NFC (MediaTek Helio G35) device. **The goal** is to move beyond heavily modified Android userlands and explore a clean, _Unix-like_ system on mobile hardware.

Alpine was chosen because of its simplicity, small footprint, and flexibility. It provides a lightweight base system that can be easily adapted for embedded devices and experimental ports. Unlike traditional Android-based distributions, Alpine gives full control over the system without unnecessary services or background overhead.

If you find any bugs, please let me know and I will try to fix them. Please note that I may be slow to respond, as I work on any projects in my free time.

## Guides
* [🇬🇧 Install EN](Docs/ins/en.md)
* [🇷🇺 Install RU](Docs/ins/ru.md)

## What works
* Booting (`OpenRC` as init-system),
* Wi-Fi (`wpa_supplicant, dhcpcd`),
* Charging status and percentage tracking,
* SSH (`openssh`),
* `apk` package manager,
* `agetty, tty, sh/bash`,
* Console cursor visibility (`fbcon`),
* USB Gadget (Serial Console `/dev/ttyGS0` via ACM for emergency debugging),
* Audio (`aplay -D hw:1,0 -d 1 -c 2 -r 44100 -f S16_LE /dev/urandom` tested, `alsamixer` configuration needed. Initial volume may be loud),
* Touchscreen (`buffyboard`),
* X11 (`X.Org, xorg-server, xf86-video-fbdev`) (not bundled by default),
  - DE's (confirmed working):
  - `XFCE4`,
  - `LXQt` (imo it works best)

## In plans
* Kernel debloat (disable heavy debugging and tracing to optimize RAM usage and speed up boot/compilation times),
* Test and configure remaining hardware (sensors, NFC, camera),
* Write a post-installation setup guide (network configuration, audio level tuning, desktop environments setup).

## Liked it?
* **KISS.**