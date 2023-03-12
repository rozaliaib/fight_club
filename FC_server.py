"""
   Сервер для консольной игры "Бойцовский клуб".

   Протокол общения:
      "_место_удара_ _защищаемое_место_"  - ход игрока

"""

from socket import *

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



    #получаем ip клиента
    ip_address = address[0]

    hit_markers = ["голова", "торс", "пояс", "ноги"]

    data_list = str_data.split()  #формируем спиоск команд от клиента
    msg_hit = int(data_list[0])   #выделяем номер места для удара
    msg_block = int(data_list[1])  #выделяем ноиер места для защиты

    #Формируем сообщение для ответа клиенту
    answer = f'Игрок 1 ударил в {hit_markers[msg_hit]} защитил {hit_markers[msg_block]} '
    #Отправляем ответ клиенту
    connection.send(answer.encode('utf-8'))
    connection.close()

