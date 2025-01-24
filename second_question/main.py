
path = "file_with_info02/byte.txt"


def get_cats_info(path):
    try:
        with open(path, "r") as info:
            # Читаем строки и разбиваем их по запятой
            lines = [line.strip().split(",") for line in info]
    except FileNotFoundError:
        return f"File {path} path is incorrect"

    # Ключи для создания словарей
    keys = ["id", "name", "age"]
    cats_info = []
    try:
        for element in lines:
            # Создаем словарь из ключей и текущей строки
            cat_dict = dict(zip(keys, element))
            cats_info.append(cat_dict)
    except IndexError:
        return "[f"
    return cats_info

print(get_cats_info(path))