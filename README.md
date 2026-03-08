# BiblioTech – system zarządzania biblioteką

Projekt zaliczeniowy z programowania w Pythonie / Django.  
Aplikacja webowa do przeglądania katalogu książek, zarządzania egzemplarzami oraz rezerwacji przez użytkowników.

## Technologie

- Python 3.11+
- Django 5
- Django REST Framework
- Bootstrap 5 (frontend)
- SQLite (środowisko deweloperskie)

## Funkcjonalności

- Przeglądanie katalogu książek (lista, szczegóły).
- Filtrowanie i wyszukiwanie książek po tytule, autorze, gatunku.
- System rejestracji i logowania użytkowników.
- Rezerwacja dostępnych egzemplarzy książek przez zalogowanych użytkowników.
- Podgląd listy własnych rezerwacji („Moje rezerwacje”).
- Panel administracyjny Django do zarządzania danymi.
- Publiczne API (Django REST Framework) dla:
  - autorów, gatunków, książek, egzemplarzy, rezerwacji,
  - dokumentacja Swagger / Redoc.

## Uruchomienie projektu (lokalnie)

1. Sklonuj repozytorium:
```bash
    git clone https://github.com/danielkasprzycki11-lab/psychic-octo-eureka.git
   cd psychic-octo-eureka/bibliotech
```

2. Utwórz i aktywuj wirtualne środowisko:
```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
```

3. Zainstaluj zależności:
```bash
    pip install -r requirements.txt
```

4. Wykonaj migracje i uruchom serwer:
```bash
    python manage.py migrate
    python manage.py runserver
```

5. Wejdź w przeglądarce na:
```bash
    http://127.0.0.1:8000/ – katalog książek,
    http://127.0.0.1:8000/admin/ – panel admina,
    http://127.0.0.1:8000/api/schema/swagger-ui/ – dokumentacja API.
```

6. Konto testowe:
```bash
    Login: student
    Hasło: StudentPass123! (przykładowe dane – można zmienić w panelu admina)
```

7. Autor:
```bash
    Projekt przygotowany przez Daniela Kasprzyckiego jako praca zaliczeniowa Kursu Python Developer organizowanego przez Learn IT.
```