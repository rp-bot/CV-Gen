# CV Gen
Updating your Résumé should be easy. In this current climate where we are learning new stuff everyday, 
adding your newly learned skills to your CV can get tedious. So I did what every Python developer does, **Spend hours trying to automate the easiest tasks**.

CV Gen is a Python program that generates a Résumé based on the Information you provide.

## Table of Contents

-   [Features](#Features)
-   [Installation](#Installation)
-   [Dependencies](#Dependencies)

## Features

-   [x] Uses a template to output all the provided information.
-   [x] Updating is very easy.
-   [ ] _A GUI is under construction for better control_
-   [X] Key/Value stored in a seperate file giving you macro control over the information you provide.

## Installation

> Installation isn't tested for cross platform yet

## Dependencies

#### Global

-   Python 3.8 +
-   Latest pip
-   [pipenv](https://github.com/rp-bot/django_checklist#pipenv-installation)

#### GUI

-   QT designer

#### Pipfile

```shell
[packages]
docxtpl = "*"
jinja2 = "*"
pyqt5 = "*"
pyqt5-tools = "*"
pymongo = "*"

[dev-packages]
ipykernel = "*"
autopep8 = "*"
```
#### Other
- /templates/*.docx/
