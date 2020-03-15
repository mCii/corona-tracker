**Context**

This project provides an admin panel which can be used to store data 
related to patients.

**API**

An api will be built and different clients can use it.

**How to run the project locally**

1- Clone the project.


_From /src directory:_

2- Install the project requirements:

```
pip install -r ../requirements/base.txt
``` 
  
3- Run migrations to create the local database:

```
python manage.py migrate
```

4- Run the server

```
python manage.py runserver
```