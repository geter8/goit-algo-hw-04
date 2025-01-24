import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)

def list_files_in_directory(path):
    # Перевіряємо чи існує зазначена директорія
    directory = Path(path)

    if not directory.is_dir():
        print(Fore.RED + f"Помилка: {path} не є дійсною директорією.")
        return

    print(Fore.GREEN + f"Содержимое директорії {path}:")

    # Перебираємо вміст директорії
    for item in directory.iterdir():
        # Якщо це папка - виводимо синім
        if item.is_dir():
            print(Fore.CYAN + f"Папка: {item.name}")
        # Якщо це файл - виводимо жовтим
        elif item.is_file():
            print(Fore.YELLOW + f"Файл: {item.name}")

# Головна частина
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Потрібно вказати шлях до директорії.")
    else:
        directory_path = sys.argv[1]
        list_files_in_directory(directory_path)
