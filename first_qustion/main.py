
path = "txt_fili_with_info/new_doc.txt" # путь к файлу

def total_salary(path):
    try:
        with open(path,"r") as info:       # Открытие и разделение файла по  запятым
            lines = [el.split(',') for el in info]
    except FileNotFoundError:               # Обработка ошибки связаной с некоректным указание пути
        return f"File {path} path is incorrect"
    sellary = [] # переменная в которую в будущем будут записаны все зарплаты
    for el in lines:
        sellary.append(float(el[1])) # добавление зарплат в список
    #return f"Загальна сума заробітної плати: {sum(sellary)} , Середня заробітна плата: {sum(sellary)/len(sellary)}"
    return f"{sum(sellary)},{sum(sellary)/len(sellary)}"
print(total_salary(path))