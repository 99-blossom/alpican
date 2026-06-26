# Установка
## Подготовка:
1. Установите MIUI 12.5 на телефон.

2. Установите `ADB` и `Fastboot` на хост-машине:
```sh
pacman -S android-tools # arch/arch based
emerge dev-util/android-tools # gentoo
apt install adb fastboot # debian/debian based
# ... в других дистрибутивах ищите пакеты вроде `android-tools`, `adb` и `fastboot`
```

3. Проверьте версии:
```sh
fastboot --version
adb --version
```

4. Убедитесь, что Ваш пользователь состоит в группе `plugdev`:
```sh
groups
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если нет, добавьте пользователя в эту группу и заново войдите в систему:
```sh
usermod -aG plugdev $USER
```
5. Убедитесь, что устройство заряжено как минимум на 25%.

## Установка
Скачайте архив по [этой](https://drive.google.com/file/d/1Kr9nITzsnQoedxKQAV0Lj__joKi8Ze6M/view?usp=sharing) ссылке.

Распакуйте архив с прошивкой. Внутри должны быть файлы: `boot.img`, `logo.bin`, `rootfs.img`, `vbmeta.img`, `lk_blossom_R.img` и скрипт установки `install.sh`.

1. Подключите устройство к компьютеру в режиме `fastboot`. Проверьте, видит ли его компьютер, командой:
```sh
fastboot devices
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Вывод должен выглядеть примерно так:
```sh
1234567890ABCBD         fastboot
```
2. Запустите скрипт установки:
```sh
./install.sh
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если получите ошибку `Permission denied`, дайте скрипту права на выполнение и запустите его снова:
```sh
chmod +x install.sh
./install.sh
```
3. Следуйте инструкциям в скрипте.

## Пароли
* root : 1
