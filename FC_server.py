"""
   Сервер для консольной игры "Бойцовский клуб".

   Протокол общения:
      "_место_удара_ _защищаемое_место_"  - ход игрока
    Регистрация клиента : 'registr' + name
   Помощь:               'help'
   Запрос информации:    'info'

"""

from socket import *

#Регистрация клиента на сервере
clients = {}
def client_reg(name, ip):
    global clients
    clients.update({ip: name})

# Ностройка сокета
socket_object = socket(AF_INET, SOCK_STREAM)
# Обработка сигналов от клиента
socket_object.bind(('', 5400))
socket_object.listen(5)# до 5 клиентов в очереди

print('Сервер - работает.')

while True:
    # Ждём соединение от клиента
    connection, address = socket_object.accept()
    # Получаем данные от клиента
    bin_data = connection.recv(1024)
    str_data = bin_data.decode('utf-8')     #1-4 1-4

    print(str_data)

    #Разбиваем входящее сообщение на параметры
    commands = str_data.split('|')


    #получаем ip клиента
    ip_address = address[0]

    if commands[0] == 'registr':
        # Регистрация клиента(пользователя)
        client_reg(commands[1], ip_address)
        answer = f'Зарегистрирован игрок по имени {clients[ip_address]}'

    else:
         hit_markers = ["голову", "торс", "пояс", "ноги"]

         data_list = str_data.split()  #формируем спиоск команд от клиента
         msg_hit = int(data_list[0])-1   #выделяем номер места для удара
         msg_block = int(data_list[1])-1  #выделяем номер места для защиты

         #Формируем сообщение для ответа клиенту
         answer = f'{clients[ip_address]} ударил в {hit_markers[msg_hit]} защитил {hit_markers[msg_block]}'


    #Отправляем ответ клиенту
    connection.send(answer.encode('utf-8'))
    connection.close()

