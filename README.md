# bulletproof-flask :sparkles:

[![MIT License](https://img.shields.io/github/license/purveshmakode24/bulletproof-flask?style=flat-square)](https://github.com/purveshmakode24/bulletproof-flask/blob/main/LICENSE)

A simple, scalable, and powerful architecture for building production ready Flask application API services.

## Introduction

This is an attempt to present a way of creating Flask API services using the best tools in the ecosystem with a good project structure that scales very well.

Feel free to explore the codebase to get the most value out of the repo.

#### Disclaimer:

This is not supposed to be a template, boilerplate or a framework. It is an opinionated guide that shows how to do some things in a certain way. You are not forced to do everything exactly as it is shown here, decide what works best for you and your team and stay consistent with your style.

#### flask-SQLAlchemy Support:

flask-SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

If you don't want to follow the generic approach to write SQL queries to interact with the DB, you can make use of SQLalchemy.

#### Directory tree structure:

    ├── config
    ├── log      # Required
    ├── services
    │      ├── controller
    │      │     ├── n1Controller.py
    │      │     ├── n2Controller.py
    │      │     ├── ...
    │      │     └── nController.py
    │      ├── dao
    │      │    ├── n1Dao.py
    │      │    ├── n2Dao.py
    │      │    ├── ...
    │      │    └── nDao.py
    │      ├── model
    │      │     ├── n1Model.py
    │      │     ├── n2Model.py
    │      │     ├── ...
    │      │     └── nModel.py
    │      ├── service
    │      │     ├── n1Service.py
    │      │     ├── n2Service.py
    │      │     ├── ...
    │      │     └── nService.py
    │      ├── ...
    │      │
    │      └── app.py
    │
    ├── requirements.txt
    ├── venv     # Optional
    ├── .gitignore
    ├── LICENSE
    └── README.md

## Installation

- Fork the repo.
- Clone the repo.
```
git clone https://github.com/purveshmakode24/bulletproof-flask.git
```
```
cd bulletproof-flask
```
- Create & Activate virtual environment.
```
python -m venv venv

venv\Scripts\activate
```
- Install dependencies.
```
pip install -r requirements.txt
```
- Modify config.ini as per your requirements.

## Running

> Note: Add log directory in root if not present.

```
cd services

python app.py [YOUR_DB_PASS]
```
- Head over to localhost:5000 in your browser.

## Contributing

Contributions are always welcome! If you have any ideas, suggestions, fixes, feel free to contribute. You can do that by going through the following steps:

1. Clone this repo
2. Create a branch: `git checkout -b your-feature`
3. Make some changes
4. Test your changes
5. Push your branch and open a Pull Request
