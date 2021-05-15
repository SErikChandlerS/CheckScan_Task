import client
import server
import threading

# Бдшку ставил на тачке линукса, и работал с ней по локальной сети, выдав тачке статический  ip в сети
# Работал через docker, так как удонбно создавать и менеджить бдшки
# В бд два столбца, numbers и id, id с параметрами not null, auto inc, unique, primary key
# Столбец numbers обладает только параметром not null


# Этот скрипт, где происходит взаимодействие и запуск приложения
# Создаются объекты класса Client и Server

process = None
client = client.Client()
server = server.Server('test-db', 'eric', '12523', '31337', '192.168.0.103')
client.createConn(('127.0.0.1', 8080))

# Функция для загрузки в thread для бесконечной генерации чисел в бд
def pushNumbers():
    while True:
        server.generateNumbers()


# Функция для выгрузки из бд и записи в файл, так же в бесконечном цикле
def writeNumbers():
    while True:
        file = open('data.txt', 'a')
        server.translateOnSocket()

        client.receiveData()

        file.write(str(client.data) + ' ')
        file.close()


# Сам запуск потоков
if __name__ == '__main__':

    if server.checkConnection():
        generate_thread = threading.Thread(target=pushNumbers)
        receive_thread = threading.Thread(target=writeNumbers)

        generate_thread.start()
        receive_thread.start()

    exit()
