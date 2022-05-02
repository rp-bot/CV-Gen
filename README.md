# <p align="center">CV Gen</p>

<p align="center">
  <img width="640" src="img/CV GEN REPO ART.png">
</h1>

Updating your Résumé should be easy. In this current climate where we are learning new stuff everyday,
adding your newly learned skills to your CV can get tedious. So I did what every Python developer does, **Spend hours trying to automate the easiest tasks**.

CV Gen is a Python program that generates a Résumé based on the Information you provide.

## Table of Contents

-   [Features](#features)
-   [Installation](#installation)
-   [Dependencies](#dependencies)
-   [Data & Privacy](#data--privacy)

## Features

-   [x] Uses a template to output all the provided information.
-   [x] Updating is very easy.
-   [x] GUI to add and remove data with ease
-   [x] Key/Value stored in a seperate file giving you macro control over the information you provide.

### Snippets

The program uses a Template and populates it Dynamically.

<!-- Put images in table -->
<div>
        <div>
            <p>
            Before
            </p>
            <img src="img/Doc_before.png" alt="before.png" style="width: 100%;
            object-fit:contain;">
        </div>
        <div>
            <p>After</p>
            <img src="img/Doc_after.png" alt="after.png" style="width: 100%;
            object-fit:contain;">
        </div>
</div>

Uses JSON

<div>
    <div>
        <img src="img/json_code.png" alt="before.png" style="width: 100%;
            object-fit:contain;">
    </div>
</div>

## Installation

> Installation isn't tested for cross platform yet

-   Download source code
-   Installation & Dependencies
    -   **Check [how-to-pipenv](https://github.com/rp-bot/django_checklist#pipenv-installation) on steps to install and use pipenv.**
    -   **Also check [Dependencies](#dependencies) for any updates.**

#### Usage

-   `run main_ui.py`
-   If you have all the stuff correctly installed, a GUI window will open up.
-   Use this interface to add all your information and click _MAKE DOCX_ button.
    > COMING SOON: Saving & Opening projects.
-   Check in the `out` directory, there you will find the file you just created.
    > NOTE: A dialog prompt to enter the output filename is not ready yet.

## Dependencies

#### Global

-   Python 3.8 +
-   Latest pip
-   [pipenv](https://github.com/rp-bot/django_checklist#pipenv-installation) - _(link leads to pipenv installation steps)_

#### GUI

-   QT5

#### Other Notes

-   `/templates/[filename].docx/` is going to be your template for what type of resume you want. Future releases will have various options
-   An executable release is in the works. Eventually pipenv or python will not be required to use.

## Data & Privacy

-   No data is collected.
-   This program runs completely offline.
