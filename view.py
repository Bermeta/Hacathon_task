import random
import json
FILE_PATH = '/home/bermet/Desktop/task_crud/data.json'
ID_FILE_PATH = '/home/bermet/Desktop/task_crud/id.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

#CRUD

def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'

def detail_product():
    data = get_data()
    try: 
        id = int(input('Введите ID ноутбука: '))
        product = list(filter(lambda x: id == x['ID'], data))
        return product [0]
    except: 
        return 'Такого ID нет!'

def get_id():
    with open(ID_FILE_PATH, 'r') as file: 
        id = int(file.read())
        id += 1
    with open (ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    try:
        product = {
            'ID': get_id(),
            'Model': input('Введите модель продукта: '),
            'year': int(input('Введите год продукта: ')),
            'description': input('Введите описание: '),
            'price': round(float(input('Введите цену продукта: ')),2)
        }
    except:
        return 'Неверные данные!'

    data.append(product)
    save_data(data)
    return 'Создан новый продукт!'


def update_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        product = list(filter(lambda x: x ['ID'] == id, data))[0]
        print(product)
        print(f'Товар для обновления {product["Model"]}')
    except Exception as error: 
        print(error)
        return 'Неверная модель продукта! '
    

    index = data.index(product)
    choice = input('Что вы хотите изменить? 1-model, 2-year, 3-description, 4-price: ')
    if choice.strip() == '1':
        data[index]['model'] = input('Введите новую модель: ')
    elif choice.strip() == '2':
        try:
            data[index]['year'] == int(input('Введите новый год: '))
        except:
            return 'Неверные значения для "year" '
    elif choice.strip() == '3':
        try:
            data[index]['description'] == (input('Введите новое описание: '))
        except: 
            return 'Неверные значения дла описания!'
    elif choice.strip() == '4':
        data[index]['price'] = round(float(input('Введите новые данные для цены: ')), 2)
    else: 
        return  'Неверное значения для обновления'

    save_data(data)
    return 'Товар обновлен!'


def delete_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        print('producta')
        product = list(filter(lambda x: x ['ID'] == id, data))[0]
        print(f'Товар для удаления {product ["Model"]}')
    except:
        return ' Неверный ID!'
    

    choice = input('Удалить этот товар (yes/no)? ')
    if choice.lower().strip() != 'yes': 
        return  'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удален!'

print(delete_product())
