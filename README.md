# CV Gen

CV Gen is a Python script that generates a Resume based on the Information you provide.

## Table of Contents

-   [Features](##Features)
-   [Installation](##Installation)
-   [Dependencies](##Dependencies)

## Features

-   [x] Uses a template to output all the provided information.
-   [x] Updating is very easy.
-   [ ] _A GUI is under construction for better control_

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

[templates]
/templates/*.docx/
```
