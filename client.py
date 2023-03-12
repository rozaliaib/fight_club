"""
   Клиент для консольной игры "Бойцовский клуб".

   Протокол общения:
"""

from socket import *

server_address = ('localhost', 5400)

print('Игра "Бойцовский клуб!"')

name = input('Введите имя для персонажа:\n')

# TODO: регистрация игрока на сервере.

while True:
    msg_hit = input('Введите место удара(1, 2, 3, 4):\n')
    # TODO: добавить поддержку help
    msg_block = input('Введите защищаемое место (1, 2, 3, 4):\n')

    #посылка для сервера вида: "_место_удара_ _защищаемое место_"
    bin_msg = bytes(msg_hit + ' ' + msg_block, 'utf-8')

    client = socket(AF_INET, SOCK_STREAM)

    try:
        # Подключаемся к серверу
        client.connect(server_address)
        # и отправляем сообщение
        client.sendall(bin_msg)
        # ждём от сервера ответ
        data = client.recv(1024)
        #Выводим ответ от сервера
        print(data.decode('utf-8'))
    except:
        print('Нет соединения с сервером')
    finally:
        #Обязательно закрываем соединение с сервером
        client.close()
