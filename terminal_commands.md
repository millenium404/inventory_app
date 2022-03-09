## Check and install the latest LTS Release of Django

```console
(venv) foo@bar:~$ pip install "Django>=3.2,<3.3"
```

## Lists all django commands

```console
(venv) foo@bar:~$ python -m django OR django-admin
```

## Start Django Project in the current directory

```console
(venv) foo@bar:~$ python -m django startproject <my_project_name> . OR django-admin startproject <my_project_name>
```

## Create requirements file

```console
(venv) foo@bar:~$ pip freeze > requirements.txt
```
