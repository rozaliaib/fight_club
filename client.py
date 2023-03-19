"""
   Клиент для консольной игры "Бойцовский клуб".

   Протокол общения:
   Регистрация клиента : 'registr|' + name
   Помощь:               'help'
   Запрос информации:    'info'
"""

from socket import *

def send_msg(msg:str):
    bin_msg = bytes(msg, 'utf-8')
    client = socket(AF_INET, SOCK_STREAM)

    try:
        # Подключаемся к серверу
        client.connect(server_address)
        # и отправляем сообщение
        client.sendall(bin_msg)
        # ждём от сервера ответ
        data = client.recv(1024)
        # Выводим ответ от сервера
        print(data.decode('utf-8'))
    except:
        print('Нет соединения с сервером')
    finally:
        # Обязательно закрываем соединение с сервером
        client.close()

server_address = ('localhost', 5400)

print('Игра "Бойцовский клуб!"')

name = input('Введите имя для персонажа:\n')

send_msg('registr|' + name)

while True:
    # Проверка на корректность данных
    step = True
    while step:
        msg_hit = input('Введите место удара(1, 2, 3, 4):\n')
        # TODO: добавить поддержку help
        msg_block = input('Введите защищаемое место (1, 2, 3, 4):\n')
        # Если удар и защита выбраны корректно - выходим из проверки
        if 0 < int(msg_hit) < 5 and 0 < int(msg_block) < 5:
            step = False
        else:
            # Оповещаем пользователя, о некорректности введенных данных
            print('Места для удара, защиты выбраны неверно')

    #посылка для сервера вида: "_место_удара_ _защищаемое место_"


    send_msg(msg_hit + ' ' + msg_block)

