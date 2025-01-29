import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)


def list_files_in_directory(path, depth=0):
    directory = Path(path)

    if not directory.is_dir():
        print(Fore.RED + f"Помилка: {path} не є дійсною директорією.")
        return

    # Відступ для візуалізації вкладеності
    indent = "  " * depth

    # Перебираємо вміст директорії
    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.CYAN + f"{indent}Папка: {item.name}")
            # Рекурсивний виклик для вкладених папок
            list_files_in_directory(item, depth + 1)
        elif item.is_file():
            print(Fore.YELLOW + f"{indent}Файл: {item.name}")


# Головна частина
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Потрібно вказати шлях до директорії.")
    else:
        directory_path = sys.argv[1]
        list_files_in_directory(directory_path)