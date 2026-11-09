# Установка (fastboot)

> [!CAUTION]
> **ПОЖАЛУЙСТА, ПРОЧИТАЙТЕ ЭТУ ИНСТРУКЦИЮ МЕДЛЕННО, ВНИМАТЕЛЬНО И ПОЛНОСТЬЮ ОТ НАЧАЛА ДО КОНЦА!! ПРЕЖДЕ ЧЕМ НАЧИНАТЬ, УБЕДИТЕСЬ, ЧТО ВЫ ПОЛНОСТЬЮ ПОНЯЛИ КАЖДЫЙ ШАГ, КАЖДОЕ ПРИМЕЧАНИЕ И ВСЕ ИНСТРУКЦИИ!! НЕ ПРОПУСКАЙТЕ НИ ОДНУ ЧАСТЬ ЭТОГО РУКОВОДСТВА, ПОСКОЛЬКУ ЭТО МОЖЕТ ПРИВЕСТИ К ОШИБКАМ ИЛИ НЕПРЕДВИДЕННЫМ ПРОБЛЕМАМ В ДАЛЬНЕЙШЕМ!!**

> [!WARNING]
> * **Сделайте резервную копию всех важных данных** с телефона до начала установки.
> * **Убедитесь, что у вас есть средства восстановления** (SP Flash Tool или `mtkclient`) и стоковая прошивка на случай хард-брика.

## Бэкап разделов

Установщик перезаписывает разделы `boot`, `vbmeta`, `lk` и `logo`, а также `userdata`, если вы не пропускаете его прошивку (см. вопрос про userdata в разделе "Установка"). Сохраните разделы заранее из Android с root-правами:

```sh
dd if=/dev/block/by-name/boot of=/sdcard/boot.img
dd if=/dev/block/by-name/lk of=/sdcard/lk.img
dd if=/dev/block/by-name/logo of=/sdcard/logo.bin
dd if=/dev/block/by-name/vbmeta of=/sdcard/vbmeta.img

dd if=/dev/block/by-name/nvdata of=/sdcard/nvdata.bin
dd if=/dev/block/by-name/nvcfg of=/sdcard/nvcfg.bin
dd if=/dev/block/by-name/nvram of=/sdcard/nvram.bin
```

> `if=` - источник (откуда читать), `of=` - файл назначения (куда сохранить). Перепутав их местами, вы перезапишете раздел, поэтому внимательно проверьте синтаксис.

> [!NOTE]
> Установщик не затрагивает `nvdata`, `nvcfg` и `nvram`. Их копии всё равно необходимы: разделы `nvdata`, `nvcfg` и `nvram` хранят IMEI.

> [!CAUTION]
> Резервные копии выше **не включают** раздел `userdata` (личные файлы, приложения, фото). Чтобы сохранить данные, скопируйте нужное заранее (через `adb pull`, MTP или облако) **до** запуска установщика.

Скопировать файлы на компьютер можно через ADB:

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

## Подготовка

1. Установите на телефон MIUI 12.5. Стоковый `boot.img` (см. раздел "Установка") берите из этой же прошивки.

2. Установите `adb` и `fastboot` на компьютер:

   ```sh
   pacman -S android-tools                      # arch и производные
   emerge dev-util/android-tools                # gentoo и производные
   apt install adb fastboot                     # debian и производные
   brew install --cask android-platform-tools   # macOS

   # в других дистрибутивах ищите пакеты android-tools, adb или fastboot
   ```

   Или скачайте platform-tools с [developer.android.com](https://developer.android.com/tools/releases/platform-tools#downloads).

3. Проверьте версии:

   ```sh
   fastboot --version
   adb --version
   ```

4. Убедитесь, что ваш пользователь входит в группу `plugdev`:

   ```sh
   groups
   ```

   Если группы нет, добавьте пользователя в неё и войдите в систему заново:

   ```sh
   usermod -aG plugdev $USER
   ```

5. Зарядите телефон минимум до 25%.

## Установка

### Получите архив

Скачайте последний архив со страницы [**Releases**](https://github.com/99-blossom/alpican/releases/latest) и распакуйте его.


### Положите стоковый boot.img

Скопируйте стоковый `boot.img` в каталог `alpican/` и переименуйте его в `boot-stock.img`. Файл должен лежать рядом с `install.sh`, а не в `images/`:

```
alpican/
├── bin/
├── boot-stock.img   ← стоковый boot.img
├── images/
├── kernel/
├── install.bat
└── install.sh
```

Без этого файла установщик завершится с ошибкой.

> [!NOTE]
> Вместе с новым ядром в образе сохраняется DTB из вашего стокового `boot.img`. Поэтому `boot-stock.img` должен быть взят с вашего телефона из той же прошивки, что на нём установлена. Образ из другой прошивки или от другой модели может не загрузиться.

### Подключите телефон

1. Переведите телефон в режим fastboot и подключите его к компьютеру.
2. Проверьте, что компьютер видит устройство:

   ```sh
   fastboot devices
   ```

   Вывод должен выглядеть примерно так:

   ```sh
   1234567890ABCBD         fastboot
   ```

### Запустите установщик

Запускайте скрипт **из каталога `alpican/`**:

Linux / macOS:

```sh
cd alpican
./install.sh
```

Если появилась ошибка `Permission denied`, сделайте скрипт исполняемым и запустите его снова:

```sh
chmod +x install.sh
./install.sh
```

Windows (cmd, из каталога `alpican\`):

```bat
install.bat
```

> [!IMPORTANT]
> Установщик на Windows работает только на x86-64. Установка с ARM64-версии Windows не поддерживается.

### Вопросы установщика

Установщик спрашивает по порядку. Ввод, отличный от допустимых значений, прерывает установку.

1. **Are you ready? [y/N]** - введите `y`, чтобы продолжить.

2. **Which LK?** - выберите загрузчик:
   * `1` - `lk_blossom_R.img`: поддержка кастомного логотипа загрузки.
   * `2` - `oem-cdms-logo-lk.img`: поддержка кастомного логотипа и исправление ошибки `dm-verity corruption`.

   > [!NOTE]
   >
   > Если выбран `oem-cdms-logo-lk.img`, идентификатор хоста может отображаться как **MT6762G**. Это ожидаемое поведение и не влияет на работу системы.
   >
   > [Причина: этот LK взят из прошивки Redmi 10A (MIUI 12.5.4.0 RCZCNXM), где используется платформенный идентификатор MT6762G, а не кодовое имя устройства.](https://4pda.to/forum/index.php?act=findpost&pid=139550809&anchor=Spoil-139550809-2)

3. **Which logo?** - выберите логотип:
   * `1` - `logo_redmi_alpine.bin`: стандартный логотип Redmi с надписью **Powered by Alpine** вместо **Android**.
   * `2` - не прошивать раздел `logo`. Выберите, если вас устраивает текущий логотип.

По завершении установки перезагрузите телефон командой:

```sh
fastboot reboot
```

> [!TIP]
> Если после прошивки `rootfs.img` в `userdata` система видит только ~500 МБ (исходный размер образа), расширьте файловую систему на весь раздел:
>
> ```sh
> resize2fs /dev/mmcblk0p41
> ```
>
> Утилита `resize2fs` входит в rootfs по умолчанию, начиная с версии 5.0.

## Пароли

* **root:** `1`