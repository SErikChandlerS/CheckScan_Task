import socket
import random
import psycopg2

# Класс сервера, с полямя : подключение к дб, сокет для серва,
# id элементов, для того чтобы доставать из базы, и два курсора
# для двух потоков

class Server:

    def __init__(self, name, user, password, port, host):
        self.conn = psycopg2.connect(dbname=name, user=user, password=password, host=host, port=port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        self.sock.bind(('', 8080))
        self.connCurs = self.conn.cursor()
        self.cursor = self.conn.cursor()
        self.dataid = 1

    def generateNumbers(self):
        # метод для генерации и загрузки данных в бд

        number = random.randint(0, 1000)
        sql = """INSERT INTO numbers VALUES(%s);"""
        self.cursor.execute(sql, (number,))
        self.conn.commit()

    def checkConnection(self):
        # метод для првоерки подключения клиента к серверу

        self.check, self.client = self.sock.recvfrom(1024)
        print(self.check.decode())
        print(self.client)
        if self.check:
            return True

    def translateOnSocket(self):
        # транслирование данных из бд на сокет клиента
        # достаю данные по одному элементу по id

        sql = "SELECT * FROM numbers WHERE id=(%s);"
        self.connCurs.execute(sql, (self.dataid,))
        data = self.connCurs.fetchone()
        self.sock.sendto(str(data[0]).encode('utf-8'), self.client)
        self.dataid += 1
