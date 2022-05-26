import nmap
import socket

class SkanerNmap:
    def __init__(self):
        self.skanerPortow = nmap.PortScanner()

    def skanujPort(self, adresHosta, port):
        host = socket.gethostbyname(adresHosta)
        self.skanerPortow.scan(host, str(port))

        self.nazwaUslugi = self.skanerPortow[host]['tcp'][port]['name']
        self.stanUslugi = self.skanerPortow[host]['tcp'][port]['state']

        print(" IP " + host + "; port TCP/" + str(port) + "; usługa: " + self.nazwaUslugi + "; stan: " + self.stanUslugi)

