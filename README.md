# bulletproof-flask :sparkles:
A simple, scalable, and powerful architecture for building production ready Flask application API services. 

> Note: Add log directory in root if not present

> Directory tree structure  
  
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
    │      │
    │      ├── ...
    │      │
    │      └── app.py
    │      
    ├── requirements.txt
    ├── venv     # Optional 
    ├── .gitignore
    ├── LICENSE
    └── README.md
