from library import Libary
from book import Book
libary = Libary()

unos = input("Sta zelite da radite (1-Za dodavanje knjige, 2-Za brisanje knjige, 3-Za menjanje informacija o knjigama, 4-Za prikaz svih knjiga): ")
if unos =="1":
    while True:
        print("Napisi informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        book = Book(naziv, autor, god_izdanja, zanr)
        libary.dodaj_knjigu(book)
        code = input("Ako zelite da prekinete upis knjiga pritisnite x ako ne bilo sta drugo")
        if code == "x":
            break
    
    with open("fajl.txt", "a") as file:
        for object in libary.lista_objekata:
            file.write(object.display_info() + "\n")


elif unos == "21":
    kriterjum = input("Po cemu zelite da pretrazujete knjige: ")
    key_word = input("Kljucna rec za pretragu: ")
    results = libary.search_books(kriterjum, key_word)
    print("Rezultati pretrage: ")
    for result in results:
        print(result)