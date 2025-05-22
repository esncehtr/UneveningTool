# UneveningTool для Infinix Note 30

**UneveningTool** — утилита для работы с Infinix Note 30 (X6833B). Разблокировка загрузчика, отключение верификации vbmeta, прошивка рекавери, MDM-байпас и установка APK — всё в одном месте. Простое меню, цветной интерфейс, поддержка Linux и Windows.

Создатель: [@sc4uz](https://t.me/sc4uz)  
Чат русского сообщества: [t.me/infinixnote30russia](https://t.me/infinixnote30russia)

## Возможности
- Разблокировка загрузчика (fastboot/oem unlock).
- Отключение верификации vbmeta (vbmeta.img для слотов a/b).
- Прошивка рекавери (TWRP, OrangeFox и др.).
- MDM-байпас (proinfo.bin).
- Установка APK.

## Требования
- **Система**:
  - Linux (Arch Linux, Ubuntu/Debian) или Windows 10/11.
- **Устройство**:
  - Infinix Note 30.
  - Включенная USB-отладка.
  - Драйверы USB для Windows.
- **Файлы**:
  - `vbmeta_verify`: `vbmeta.img`, `vbmeta_system.img`, `vbmeta_vendor.img`.
  - `recovery`: `.img` файлы рекавери.
  - `mdm`: `proinfo.bin` для MDM-байпаса.
  - `apk`: `.apk` файлы.
- **Зависимости**:
  - Python 3.8+.
  - `colorama` (для цветного интерфейса).
  - ADB и Fastboot (platform-tools).

## Установка и запуск

### Linux (Arch Linux, Ubuntu/Debian)
1. Скачайте сам скрипт
2. Сделайте скрипт установки исполняемым:
   ```bash
   chmod +x install.sh
   ```
3. Запустите установку:
   ```bash
   ./install.sh
   ```
   Установятся Python, `colorama`, ADB, Fastboot.
4. Запустите:
   ```bash
   python3 tool.py
   ```

### Windows
1. Скачайте сам скрипт
2. Установите Python 3.8+:
   - [python.org](https://www.python.org/downloads/windows/).
   - Добавьте Python в PATH при установке.
3. Установите `colorama`:
   ```cmd
   pip install colorama
   ```
4. Установите ADB и Fastboot:
   - Скачайте [platform-tools](https://developer.android.com/studio/releases/platform-tools).
   - Добавьте папку с `adb.exe` и `fastboot.exe` в PATH или поместите в папку с утилитой.
5. Создайте папки `vbmeta_verify`, `recovery`, `mdm`, `apk` в папке с `UneveningTool_Windows.py`.
6. Поместите файлы в папки (см. ниже).
7. Запустите:
   ```cmd
   python tool.py
   ```

## Где взять файлы
- **vbmeta**: Стоковая прошивка Infinix Note 30 с [needrom.com](https://needrom.com) или [4PDA](https://4pda.to).
- **Рекавери**: TWRP/OrangeFox на [4PDA](https://4pda.to) или [xda-developers.com](https://xda-developers.com).
- **apk**: Совместимые `.apk` (например, от проверенных источников).

## Использование
1. Запустите утилиту (`python3 tool.py` или `python tool.py`).
2. Выберите действие в меню:
   - **1. Разблокировка загрузчика**: Удаляет данные, требует Infinix ID.
   - **2. Отключение верификации vbmeta**: Прошивает vbmeta для слотов a/b.
   - **3. Прошивка рекавери**: Выберите `.img` из папки `recovery`.
   - **4. MDM-байпас**: Прошивает `proinfo.bin`.
   - **5. Установка APK**: Выберите `.apk` из папки `apk`.
   - **6. Информация и ссылки**: Ссылки на сообщества.
   - **7. Выход**.
3. Следуйте подсказкам (например, нажмите громкость "+" для разблокировки).

## Предупреждения
- **Разблокировка загрузчика**: Удаляет все данные. Сделайте бэкап.
- **MDM-байпас**: На новых версиях XOS может вызвать Red State
- **Infinix ID**: После разблокировки может потребоваться ожидание 7–14 дней.

## Возможные проблемы
- **ADB/Fastboot не найдены**:
  - Linux: Проверьте установку (`adb devices`).
  - Windows: Добавьте platform-tools в PATH.
- **Colorama не работает**:
  - Linux: Убедитесь, что `python-colorama` установлен.
  - Windows: Установите `pip install colorama`.
- **Устройство не определяется**:
  - Включите USB-отладку.
  - Windows: Установите USB-драйверы для Infinix Note 30.
- **Неподдерживаемый дистрибутив**:
  Для Fedora и других:
  ```bash
  sudo dnf install python3 python3-pip android-tools python3-colorama
  ```

## Поддержка
- Создатель: [@sc4uz](https://t.me/sc4uz)
- Чат Infinix Note 30: [t.me/infinixnote30russia](https://t.me/infinixnote30russia)
