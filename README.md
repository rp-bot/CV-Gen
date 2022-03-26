# CV Gen

Updating your Résumé should be easy. In this current climate where we are learning new stuff everyday,
adding your newly learned skills to your CV can get tedious. So I did what every Python developer does, **Spend hours trying to automate the easiest tasks**.

CV Gen is a Python program that generates a Résumé based on the Information you provide.

## Table of Contents

-   [Features](#Features)
-   [Installation](#Installation)
-   [Dependencies](#Dependencies)
-   [Data & Privacy](#data--privacy)

## Features

-   [x] Uses a template to output all the provided information.
-   [x] Updating is very easy.
-   [ ] GUI to add and remove data with ease
-   [x] Key/Value stored in a seperate file giving you macro control over the information you provide.

### Snippets

The program uses a Template and populates it Dynamically.

<style>
        .row {
            display: flex;
            text-align: center;
            padding-left:80px;
            padding-right:80px;
            padding-bottom:40px;
        }

        .column {
            flex: 33.33%;
            margin-left: 2.5px;
            margin-right: 2.5px;
            border-style: solid;
            border-width: 1px;
        }

        .doc_img {
            width: 100%;
            object-fit:contain;
        }

        .doc_header {
            margin: 0;
            padding:0;
            border-style: solid;
            border-width: 1px;
            border-left: 0px;
            border-right: 0px;
            border-top: 0px;
            background-color:rgb(204, 204, 204);
        }
</style>

<div class="row">
        <div class="column">
            <p class="doc_header">Before</p>
            <img src="img/Doc_before.png" alt="before.png" class="doc_img">
        </div>
        <div class="column">
            <p class="doc_header">After</p>
            <img src="img/Doc_after.png" alt="after.png" class="doc_img">
        </div>
</div>

Uses JSON as a database

<div class="row">
    <div class="column">
        <img src="img/json_code.png" alt="before.png" class="doc_img">
    </div>
</div>

## Installation

> Installation isn't tested for cross platform yet

## Dependencies

#### Global

-   Python 3.8 +
-   Latest pip
-   [pipenv](https://github.com/rp-bot/django_checklist#pipenv-installation) - _(link leads to pipenv installation steps)_

#### GUI

-   QT designer

#### Other

-   /templates/\*.docx/

## Data & Privacy
