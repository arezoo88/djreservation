<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Hotel Reservation</h3>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Document](#document)
- [AdminPanel](#admin)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This project is done for testing.(Reservation)

## 🏁 Getting Started <a name = "getting_started"></a>

- virtualenv -p python3 .env
- source env/bin/activate

### Installing

- pip install -r requirements.txt
- python manage.py makmeigrations
- python manage.py migrate
- python manage.py loaddata fixtures/db.json
- python manage.py runserver

## Document <a name = "document"></a>

- http://127.0.0.1:8000/ or http://127.0.0.1:8000/redoc/
- if open this url (http://127.0.0.1:8000/swagger.json) you can get json file and open in this site : https://editor.swagger.io/

## Admin Panel <a name="admin"></a>

- python manage.py createsuperuser
- http://127.0.0.1:8000/admin/

## 🔧 Running the tests <a name = "tests"></a>

- python manage.py loaddata  fixtures/db.json
- python manage.py test reservation.test_views

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
in these tests...
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Sqlite](https://www.sqlite.org/index.html) - Sqlite
- [Django](https://www.djangoproject.com/) - Server Framework

## ✍️ Authors <a name = "authors"></a>

- [@arezoo88](https://github.com/arezoo88)
