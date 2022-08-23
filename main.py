'''
CRUD

create 
read - retrive
update
delete 
'''


import shelve
from datetime import datetime

from settings import FILENAME


'''
db = {
    '45372': {
        'title': 'Apple Iphone 13',
        'price': 29999,
        'description': 'Very good phone',
        'created_at': '23.08.22 18:54'
    }
}
'''


def create():
    '''создает новый товар'''
    id_ = datetime.now().strftime('%H%M%S')
    title = input('введите название  товар: ')
    price = int(input('введите цену товарa: '))
    description = input('введите описание  товарa: ')
    created_at = datetime.now().strftime('%d.%m.%y %H:%M')
    with shelve.open(FILENAME) as db:
        db[id_] = {
            'title': title,
            'price': price,
            'description' : description,
            'created_at': created_at
        }

def get_all_data():
    '''выводит список товаров'''
    with shelve.open(FILENAME) as db:
        print('\nсписок товаров:')
        for key, value in db.items():
            print('-' * 75)
            print('id товара:', key, '\nназвание товара:', value['title'], '\nцена товара::', value['price'],'$',
            '\nописание товара:',  value['description'])
            print('-' * 75)            


def get_data_by_id():
    '''выводит товар по id'''
    id_ = input('\nВведите id товара: ')
    retrive()
    with shelve.open(FILENAME) as db:
        try:
            prod = db[id_]
            print(
                f"""  
                Название: {prod['title']}
                Цена: {prod['price']}
                Описание: {prod['description']}
                Время создания: {prod['created_at']}
                """
            )
        except KeyError:
            print(f'{id_} не существует')

def update_data():
    '''изменяет данные'''
    retrive()
    id_ = input('введите id товара: ')
    with shelve.open(FILENAME, writeback=True) as db:
        try:
            prod = db[id_]
            prod['title'] = input('введите новое название товара: ') or prod['title']
            prod['price'] = input('введите новую цену: ') or prod['price']
            prod['description'] = input('введите новое описание: ') or prod['description']
            print('^' * 75)
            print('данные товара успешно изменены:)'.upper())
            print('^' * 75)
        except KeyError:
            print(f'{id_} не существует')

def delete_data():
    '''удаляет товар по id'''
    retrive()
    id_ = input('введите id товара: ')
    with shelve.open(FILENAME, writeback=True) as db:
        yes_no = input('если вы уверены, введите Yes/Да или No/Нет: ').lower()
        if yes_no.lower() in 'yes, да':
            try:
                db.pop(id_)
                print('^' * 75)
                print('товар успешно удален:)'.upper())
                print('^' * 75)
            except KeyError:
                print(f'{id_} не существует')
        else: 
            print('^' * 75)
            print('товара НЕ удален')
            print('^' * 75)


def info():
    '''выводит список операций'''
    print('\nсписок операций, которые вы можете совершить:')
    print(
        '''
        1. create - создать новый товар
        2. update - изменить данные товара
        3. delete - удалить товар по id
        4. retrive - получить товар по id 
        5. list - список всех товаров
        7. exit - выйти из программы
        '''
    )
 
def retrive():
    '''выводит доступные id'''
    with shelve.open(FILENAME) as db:
        for key in db:
            print('=' * 75)
            print(f'доступный id: {key}')


def main_func():
    '''выполняет операции'''
    while True:
        info()
        inp = input('введите операцию: ').lower()
        if inp == 'create':
            create()
        elif inp == 'update':
            update_data()
        elif inp == 'delete':
            delete_data()
        elif inp == 'retrive':
            retrive()
            get_data_by_id()
        elif inp == 'list':
            get_all_data()
        elif inp == 'exit':
            print('-----GOODBYE:)-----')
            break
        else:
            print('\nтакой команды не существует!!!'.upper())
            
