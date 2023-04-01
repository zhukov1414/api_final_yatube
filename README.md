# **Проект «API для Yatube**.

## **Описание**
### API для Yatub проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Стек технологий

* Python 3.11,
* Django 4.2,
* DRF,
* JWT + Djoser

### **Как запустить проект**:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:zhukov1414/api_final_yatube.git
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
