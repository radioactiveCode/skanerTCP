from skanujPorty import SkanerNmap

def wczytajDane():

    # wprowadzanie adresu hosta
    adresHosta = input("\nPodaj adres hosta: ")

    # określanie trybu pracy skanera
    while True:
        trybSkanowania = input("Wybierz tryb skanowania (1 - skanowanie wybranych portów, "
                               "2 - skanowanie zakresu portów): ")
        if ((trybSkanowania == "1") or (trybSkanowania == "2")):
            break

    # wprowdzanie numerów portów i zatwierdzenie
    if trybSkanowania == "1":
        wczytajWybranePorty(adresHosta)
    else:
        wczytajZakresyPortow(adresHosta)

def wczytajWybranePorty(adresHosta):
    portyHosta = input("Podaj numery portów rozdzielone przecinkiem: ")
    input("\nAby rozpocząć skanowanie naciśnij Enter\n")
    portyHosta = portyHosta.split(",")
    for port in portyHosta:
        SkanerNmap().skanujPort(adresHosta, int(port))

def wczytajZakresyPortow(adresHosta):
    portStart = input("Podaj numer portu startowego: ")
    portStop = input("Podaj numer portu końcowego: ")
    input("\nAby rozpocząć skanowanie naciśnij Enter\n")
    for port in range(int(portStart), int(portStop)):
        SkanerNmap().skanujPort(adresHosta, port)