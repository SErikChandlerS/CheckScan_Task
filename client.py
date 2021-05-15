import socket

# Класс клиента, работа с модулем socket,
# работает по протоколу UDP

class Client():
    def __init__(self):
        # Создаем сокет как поле класса, и объявляем его клиентом

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
        self.sock.bind(('', 0))

    def createConn(self, server):
        # Метод для того чтобы проверить подключение к серверу

        self.sock.sendto(('Connected to server').encode('utf-8'), server)

    def receiveData(self):
        # Метод, для загружения в thread и принятия потока данных с сервера

        self.data = (self.sock.recv(1024)).decode()






