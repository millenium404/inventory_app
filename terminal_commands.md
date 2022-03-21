### Check and install the latest LTS Release of Django

```console
(venv) foo@bar:~$ pip install "Django>=3.2,<3.3"
```

### Lists all django commands

```console
(venv) foo@bar:~$ python -m django OR django-admin
```

### Start Django Project in the current directory

```console
(venv) foo@bar:~$ python -m django startproject <my_project_name> . OR django-admin startproject <my_project_name>
```

### Create requirements file

```console
(venv) foo@bar:~$ pip freeze > requirements.txt
```

### Create new component/app in Django

```console
(venv) foo@bar:~$ python manage.py startapp articles
```

### Create and update Database in Django

```console
(venv) foo@bar:~$ python manage.py makemigrations
(venv) foo@bar:~$ python manage.py migrate
```
### Read key-value pairs from a .env file and set them as environment variables.

```console
(venv) foo@bar:~$ pip install django-dotenv
```
##### In manage.py:

```python
import dotenv
def main():
    """Run administrative tasks."""
    dotenv.read_dotenv()
```

##### In settings.py:

```python
import os
DEBUG = str(os.environ.get('DEBUG')) == '1'
```

### Install </> htmx for django

```console
(venv) foo@bar:~$ pip install django-htmx
```

```console
Add django_htmx to INSTALLED_APPS and django_htmx.middleware.HtmxMiddleware to MIDDLEWARE in settings.py
```
