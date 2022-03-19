# Introduction

This project requires the following tools:

- Python - The programming language used by Flask.
- PostgreSQL - A relational database system.
- Virtualenv - A tool for creating isolated Python environments.


## Getting started

**Step 1. Clone the code into a fresh folder**
```
git clone https://github.com/jsrdriguez/base-python-flask.git
cd base-python-flask
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/). Learn more about [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

```
$ python -m venv .venv
$ source .venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```