import threading
from socket import *
import json


nickname = []
clients = []
pole = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
xod = [1, 0]
WIN = [False]

class Server:





    def __init__(self, ip, port):
        print(f"SERVER IP: {ip}\n SERVER PORT: {port}")
        self.ser = socket(AF_INET, SOCK_STREAM)
        self.ser.bind((ip, 2000))
        self.ser.listen(2)
        self.start_server()








    def obrabotka(self, user, otvet):
        if(len(clients) == 2):
            if(pole[otvet] == -1):
                if(xod[clients.index(user)] == 1):
                    xod[0] = 1
                    xod[1] = 1
                    xod[clients.index(user)] = 0
                    pole[otvet] = clients.index(user)
                    stroka = str(otvet)
                    self.sender(user, stroka)
                    print(pole)
                    self.Vinners(user)
                else: self.sender(user, "Ne Vash hod")
            else:
                self.sender(user, "Zaneto")







    def Vinners(self, user):
        if (pole[0] == clients.index(user) and pole[3] == clients.index(user) and pole[6] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[1] == clients.index(user) and pole[4] == clients.index(user) and pole[7] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[2] == clients.index(user) and pole[5] == clients.index(user) and pole[8] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[0] == clients.index(user) and pole[1] == clients.index(user) and pole[2] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[3] == clients.index(user) and pole[4] == clients.index(user) and pole[5] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[6] == clients.index(user) and pole[7] == clients.index(user) and pole[8] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[0] == clients.index(user) and pole[4] == clients.index(user) and pole[8] == clients.index(user)):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()

        if (pole[2] == clients.index(user) and pole[4] == 1 and pole[6] == 1):
            self.sender(user, "VIN " + nickname[clients.index(user)])
            self.VinnersUser()



    def VinnersUser(self):
        pole[0] = -1
        pole[1] = -1
        pole[2] = -1
        pole[3] = -1
        pole[4] = -1
        pole[5] = -1
        pole[6] = -1
        pole[7] = -1
        pole[8] = -1






    def sender(self, user, text):
        for user in clients:
            user.send(text.encode('utf-8'))














    def start_server(self):
        while True:
            user, addr = self.ser.accept()
            print(f"CONNECT. IP: {addr[0]}\n\tPORT: {addr[1]}")
            names = user.recv(1024)
            nickname.append(format(str(names.decode('utf-8'))))

            clients.append(user)  # Добавление в списки клиентов
            print(len(clients))
            print(format(str(nickname)))
            thread = threading.Thread(target=self.listen, args=(user, ))  # Запуск многопоточности
            thread.start()  # Старт многопоточности












    def listen(self, user):
        self.sender(user, "Connect\t")
        is_work = True
        while is_work:
            try:
                data = user.recv(1024)
                #self.sender(user, data.decode('utf-8'))
                test = True
                i = 0
                text = data.decode('utf-8')
                while test:
                    if(text[i] == ":"):

                        otv = text[i+1: len(text)]
                        test = False
                    i += 1
                    if(i == len(text)):
                        test = False
                        otv = ""
                try:
                    otv = str(otv.encode('utf-8'))
                    otv = "b'" +otv[8:12] + "'"
                    self.Raspozn(otv, user)
                except Exception as es:
                    print(es)
                    nickname.pop()
                    clients.remove(user)
            except Exception as e:
                print(str(e))
                is_work = False














    def Raspozn(self, otv, user):
        if (otv != ""):
            if (str(otv) == "b'x001'"):
                self.obrabotka(user, 1)

            if (str(otv) == "b'x002'"):
                self.obrabotka(user, 2)

            if (str(otv) == "b'x003'"):
                self.obrabotka(user, 3)

            if (str(otv) == "b'x004'"):
                self.obrabotka(user, 4)

            if (str(otv) == "b'x005'"):
                self.obrabotka(user, 5)

            if (str(otv) == "b'x006'"):
                self.obrabotka(user, 6)

            if (str(otv) == "b'x007'"):
                self.obrabotka(user, 7)

            if (str(otv) == "b'x008'"):
                self.obrabotka(user, 8)

            if (str(otv) == "b'x000'"):
                self.obrabotka(user, 0)






Server('212.76.128.141', 2000)