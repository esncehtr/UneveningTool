import os
import subprocess
from time import sleep
from colorama import init, Fore, Style

init()

def banner():
    print(f"""
    {Fore.CYAN}╔═══════════════════════════════════════╗
    ║ UneveningTool for Infinix Note 30     ║
    ║ Создатель: @sc4uz                     ║
    ║ Контрибьютор: @DETCKUE_TPABMbI        ║
    ╚═══════════════════════════════════════╝{Style.RESET_ALL}
    """)

def progress(step, total):
    bar = f"{Fore.GREEN}[{'=' * int(step/total*20)}{' ' * (20-int(step/total*20))}]"
    print(f"{bar} Шаг {step}/{total}")

def clear():
    os.system("cls")

def check_adb():
    try:
        subprocess.run(["adb", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["fastboot", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{Fore.GREEN}ADB и Fastboot найдены.")
        return True
    except:
        print(f"{Fore.RED}ADB или Fastboot не установлены.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        return False

def device():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)
        if len(result.stdout.splitlines()) > 1 and "device" in result.stdout:
            model = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
            print(f"{Fore.GREEN}Устройство: {model}")
            return model
        print(f"{Fore.RED}Устройство не подключено.")
        return None
    except:
        print(f"{Fore.RED}Ошибка проверки устройства.")
        return None

def unlock():
    print(f"{Fore.YELLOW}Разблокировка загрузчика. Данные будут удалены.")
    if input("Продолжить? (y/n): ").lower() != 'y':
        print("Операция отменена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if device():
        progress(1, 4)
        subprocess.run(["adb", "reboot", "bootloader"])
        sleep(10)
        print(f"{Fore.YELLOW}Нажмите громкость '+'...")
        progress(2, 4)
        try:
            subprocess.run(["fastboot", "flashing", "unlock"], check=True)
            print(f"{Fore.GREEN}Разблокировка успешна.")
        except:
            print(f"{Fore.YELLOW}Пробуем другой метод...")
            progress(3, 4)
            try:
                subprocess.run(["fastboot", "oem", "unlock"], check=True)
                print(f"{Fore.GREEN}Разблокировка успешна.")
            except:
                print(f"{Fore.RED}Ошибка. Проверьте Infinix ID.")
                input(f"{Fore.YELLOW}Нажмите Enter...")
                clear()
                return
        progress(4, 4)
        subprocess.run(["fastboot", "reboot"])
        print(f"{Fore.GREEN}Перезагрузка...")
    else:
        print(f"{Fore.RED}Устройство не найдено.")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def vbmeta():
    folder = "vbmeta_verify"
    files = ["vbmeta.img", "vbmeta_system.img", "vbmeta_vendor.img"]
    print(f"{Fore.YELLOW}Отключение верификации vbmeta...")
    
    if not os.path.exists(folder):
        print(f"{Fore.RED}Папка {folder} не найдена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    for file in files:
        if not os.path.exists(os.path.join(folder, file)):
            print(f"{Fore.RED}Файл {file} не найден.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()
            return
    
    if input("Режим bootloader, Enter (n - отменить): ").lower() == 'n':
        print("Операция отменена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    total = len(files) * 2
    step = 0
    try:
        for slot in ['a', 'b']:
            for file, part in zip(files, ['vbmeta', 'vbmeta_system', 'vbmeta_vendor']):
                step += 1
                progress(step, total)
                subprocess.run(["fastboot", "--disable-verity", "--disable-verification", "flash", f"{part}_{slot}", os.path.join(folder, file)], check=True)
        print(f"{Fore.GREEN}Верификация отключена.")
        subprocess.run(["fastboot", "reboot"])
        print(f"{Fore.GREEN}Перезагрузка...")
    except:
        print(f"{Fore.RED}Ошибка отключения верификации.")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def recovery():
    folder = "recovery"
    print(f"{Fore.YELLOW}Прошивка рекавери...")
    
    if not os.path.exists(folder):
        print(f"{Fore.RED}Папка {folder} не найдена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    imgs = [f for f in os.listdir(folder) if f.endswith(".img")]
    if not imgs:
        print(f"{Fore.RED}Нет .img файлов.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    print("Файлы рекавери:")
    for i, file in enumerate(imgs, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input("Выберите номер (0 - выход): ")) - 1
        if choice == -1:
            print("Выход.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()
            return
        if choice < 0 or choice >= len(imgs):
            print(f"{Fore.RED}Неверный выбор.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()
            return
        file = os.path.join(folder, imgs[choice])
    except:
        print(f"{Fore.RED}Некорректный ввод.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if device():
        progress(1, 3)
        subprocess.run(["adb", "reboot", "bootloader"])
        sleep(10)
        progress(2, 3)
        try:
            subprocess.run(["fastboot", "flash", "recovery", file], check=True)
            print(f"{Fore.GREEN}Рекавери прошито.")
            progress(3, 3)
            subprocess.run(["fastboot", "reboot"])
            print(f"{Fore.GREEN}Перезагрузка...")
        except:
            print(f"{Fore.RED}Ошибка прошивки.")
    else:
        print(f"{Fore.RED}Устройство не найдено.")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def mdm():
    folder = "mdm"
    file = "proinfo.bin"
    path = os.path.join(folder, file)
    print(f"{Fore.YELLOW}MDM-байпас...")
    
    if not os.path.exists(folder):
        print(f"{Fore.RED}Папка {folder} не найдена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if not os.path.exists(path):
        print(f"{Fore.RED}Файл {file} не найден.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if input("Режим bootloader, Enter (n - отменить): ").lower() == 'n':
        print("Операция отменена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if device():
        progress(1, 3)
        subprocess.run(["adb", "reboot", "bootloader"])
        sleep(10)
        progress(2, 3)
        try:
            subprocess.run(["fastboot", "flash", "proinfo", path], check=True)
            print(f"{Fore.GREEN}MDM-байпас выполнен.")
            progress(3, 3)
            subprocess.run(["fastboot", "reboot"])
            print(f"{Fore.GREEN}Перезагрузка...")
        except:
            print(f"{Fore.RED}Ошибка прошивки.")
    else:
        print(f"{Fore.RED}Устройство не найдено.")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def apk():
    folder = "apk"
    print(f"{Fore.YELLOW}Установка APK...")
    
    if not os.path.exists(folder):
        print(f"{Fore.RED}Папка {folder} не найдена.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    apks = [f for f in os.listdir(folder) if f.endswith(".apk")]
    if not apks:
        print(f"{Fore.RED}Нет .apk файлов.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    print("APK файлы:")
    for i, file in enumerate(apks, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input("Выберите номер (0 - выход): ")) - 1
        if choice == -1:
            print("Выход.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()
            return
        if choice < 0 or choice >= len(apks):
            print(f"{Fore.RED}Неверный выбор.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()
            return
        file = os.path.join(folder, apks[choice])
    except:
        print(f"{Fore.RED}Некорректный ввод.")
        input(f"{Fore.YELLOW}Нажмите Enter...")
        clear()
        return
    
    if device():
        progress(1, 2)
        try:
            subprocess.run(["adb", "install", file], check=True)
            print(f"{Fore.GREEN}APK установлен.")
            progress(2, 2)
        except:
            print(f"{Fore.RED}Ошибка установки.")
    else:
        print(f"{Fore.RED}Устройство не найдено.")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def links():
    print(f"{Fore.CYAN}=== Информация и ссылки ===")
    print("Создатель: t.me/sc4uz")
    print("Чат Infinix Note 30: t.me/infinixnote30russia")
    input(f"{Fore.YELLOW}Нажмите Enter...")
    clear()

def menu():
    while True:
        banner()
        print(f"\n{Fore.CYAN}=== UneveningTool for Infinix Note 30 ===")
        print("1. Разблокировать загрузчик")
        print("2. Отключить верификацию vbmeta")
        print("3. Прошить рекавери")
        print("4. Выполнить MDM-байпас")
        print("5. Установить APK")
        print("6. Информация и ссылки")
        print("7. Выход")
        choice = input(f"{Fore.YELLOW}Выберите (1-7): ")
        
        clear()
        if choice == "1":
            unlock()
        elif choice == "2":
            vbmeta()
        elif choice == "3":
            recovery()
        elif choice == "4":
            mdm()
        elif choice == "5":
            apk()
        elif choice == "6":
            links()
        elif choice == "7":
            print(f"{Fore.GREEN}Выход.")
            break
        else:
            print(f"{Fore.RED}Неверный выбор.")
            input(f"{Fore.YELLOW}Нажмите Enter...")
            clear()

def main():
    clear()
    if not check_adb():
        exit(1)
    menu()

if __name__ == "__main__":
    main()
