import sqlite3

# ----- KOD STARTOWY DO ZADAŃ -----
def przygotuj_baze():
    """Tworzy i wypełnia bazę danych na potrzeby zadań."""

    conn = sqlite3.connect('sklep.db')  # Tworzy plik sklep.db
    cursor = conn.cursor()

    # Usunięcie tabel, jeśli istnieją, dla czystego startu
    cursor.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
    cursor.execute("DROP TABLE IF EXISTS Zamowienia")
    cursor.execute("DROP TABLE IF EXISTS Produkty")
    cursor.execute("DROP TABLE IF EXISTS Kategorie")
    cursor.execute("DROP TABLE IF EXISTS Klienci")

    # Tworzenie tabel
    cursor.execute('''
    CREATE TABLE Kategorie (
        id_kategorii INTEGER PRIMARY KEY,
        nazwa_kategorii TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE Produkty (
        id_produktu INTEGER PRIMARY KEY,
        nazwa_produktu TEXT NOT NULL,
        cena REAL NOT NULL,
        id_kategorii INTEGER,
        FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Klienci (
        id_klienta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE Zamowienia (
        id_zamowienia INTEGER PRIMARY KEY,
        id_klienta INTEGER,
        data_zamowienia DATE,
        FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Zamowienia_Produkty (
        id_zamowienia INTEGER,
        id_produktu INTEGER,
        ilosc INTEGER NOT NULL,
        PRIMARY KEY (id_zamowienia, id_produktu),
        FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
        FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu)
    )
    ''')

    # Wstawianie danych
    kategorie = [('Elektronika',), ('Książki',), ('Dom i ogród',)]
    klienci = [('Anna Nowak', 'anna.n@example.com'),
               ('Jan Kowalski', 'jan.k@example.com'),
               ('Zofia Wiśniewska', 'zofia.w@example.com')]
    produkty = [
        ('Laptop Pro', 5200.00, 1),
        ('Smartfon X', 2500.00, 1),
        ('Python dla każdego', 89.99, 2),
        ('Wzorce projektowe', 120.50, 2),
        ('Kosiarka elektryczna', 750.00, 3),
        ('Zestaw narzędzi', 300.00, 3),
        ('Słuchawki bezprzewodowe', 450.00, 1)
    ]
    zamowienia = [(1, '2023-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
    zamowienia_produkty = [
        (1, 1, 1),  # Zamówienie 1: 1x Laptop Pro
        (1, 7, 1),  # Zamówienie 1: 1x Słuchawki bezprzewodowe
        (2, 3, 2),  # Zamówienie 2: 2x Python dla każdego
        (3, 5, 1)   # Zamówienie 3: 1x Kosiarka elektryczna
    ]

    cursor.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)", kategorie)
    cursor.executemany("INSERT INTO Klienci (imie, email) VALUES (?, ?)", klienci)
    cursor.executemany("INSERT INTO Produkty (nazwa_produktu, cena, id_kategorii) VALUES (?, ?, ?)", produkty)
    cursor.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia) VALUES (?, ?)", zamowienia)
    cursor.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia, id_produktu, ilosc) VALUES (?, ?, ?)", zamowienia_produkty)

    conn.commit()
    conn.close()
    print("Baza 'sklep.db' została przygotowana.")

# Zadanie 1: Liczba produktów
def zadanie_1():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Produkty")
    liczba = cursor.fetchone()[0]
    conn.close()
    print(f"1. Liczba produktów: {liczba}")

# Zadanie 2: Najdroższy produkt
def zadanie_2():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nazwa_produktu, cena FROM Produkty ORDER BY cena DESC LIMIT 1")
    produkt = cursor.fetchone()
    conn.close()
    print(f"2. Najdroższy produkt: {produkt[0]}, cena: {produkt[1]:.2f} zł")

# Zadanie 3: Suma wartości elektroniki
def zadanie_3():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(p.cena)
        FROM Produkty p
        JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = 'Elektronika'
    """)
    suma = cursor.fetchone()[0]
    conn.close()
    print(f"3. Łączna wartość elektroniki: {suma:.2f} zł")

# Zadanie 4: Średnia cena książki
def zadanie_4():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT AVG(p.cena)
        FROM Produkty p
        JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = 'Książki'
    """)
    avg = cursor.fetchone()[0]
    conn.close()
    print(f"4. Średnia cena książki: {avg:.2f} zł")

# Zadanie 5: Lista klientów
def zadanie_5():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("SELECT imie, email FROM Klienci")
    klienci = cursor.fetchall()
    conn.close()
    print("5. Lista klientów:")
    for imie, email in klienci:
        print(f"   {imie} - {email}")

# Zadanie 6: Produkty droższe od średniej
def zadanie_6():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nazwa_produktu, cena FROM Produkty
        WHERE cena > (SELECT AVG(cena) FROM Produkty)
    """)
    produkty = cursor.fetchall()
    conn.close()
    print("6. Produkty droższe niż średnia cena:")
    for nazwa, cena in produkty:
        print(f"   {nazwa} - {cena:.2f} zł")

# Zadanie 7: Zamówienia Anny Nowak
def zadanie_7():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.nazwa_produktu, zp.ilosc
        FROM Klienci k
        JOIN Zamowienia z ON k.id_klienta = z.id_klienta
        JOIN Zamowienia_Produkty zp ON z.id_zamowienia = zp.id_zamowienia
        JOIN Produkty p ON zp.id_produktu = p.id_produktu
        WHERE k.imie = 'Anna Nowak'
    """)
    produkty = cursor.fetchall()
    conn.close()
    print("7. Produkty zamówione przez Annę Nowak:")
    for nazwa, ilosc in produkty:
        print(f"   {nazwa} x {ilosc}")

# Zadanie 8: Kategorie z liczbą produktów
def zadanie_8():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT k.nazwa_kategorii, COUNT(p.id_produktu) 
        FROM Kategorie k
        LEFT JOIN Produkty p ON k.id_kategorii = p.id_kategorii
        GROUP BY k.id_kategorii
    """)
    dane = cursor.fetchall()
    conn.close()
    print("8. Kategorie i liczba produktów w każdej z nich:")
    for kategoria, liczba in dane:
        print(f"   {kategoria}: {liczba}")

# Zadanie 9: Funkcja wyszukiwania produktów po kategorii
def znajdz_produkty_w_kategorii(nazwa_kategorii):
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.nazwa_produktu, p.cena
        FROM Produkty p
        JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = ?
    """, (nazwa_kategorii,))
    produkty = cursor.fetchall()
    conn.close()
    return produkty

# Zadanie 10: Prosta symulacja ORM - klasa Produkt
class Produkt:
    def __init__(self, id_produktu, nazwa, cena):
        self.id_produktu = id_produktu
        self.nazwa = nazwa
        self.cena = cena

def pobierz_produkty_orm():
    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_produktu, nazwa_produktu, cena FROM Produkty")
    dane = cursor.fetchall()
    conn.close()
    return [Produkt(*row) for row in dane]

# Główne wywołanie programu
if __name__ == "__main__":
    przygotuj_baze()
    zadanie_1()
    print()
    zadanie_2()
    print()
    zadanie_3()
    print()
    zadanie_4()
    print()
    zadanie_5()
    print()
    zadanie_6()
    print()
    zadanie_7()
    print()
    zadanie_8()
    print()
    print("9. Produkty w kategorii 'Elektronika':")
    produktty_elektronika = znajdz_produkty_w_kategorii("Elektronika")
    for nazwa, cena in produktty_elektronika:
        print(f"   {nazwa} - {cena:.2f} zł")
    print()
    print("10. Produkty jako obiekty ORM:")
    produkty = pobierz_produkty_orm()
    for produkt in produkty:
        print(f"   ID: {produkt.id_produktu}, Nazwa: {produkt.nazwa}, Cena: {produkt.cena:.2f} zł")
