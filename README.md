#  To Run the project 

### Clone the Project in your local enviornment

` git@github.com:ritikchauhan-01/dashboard.git `

### Run The migrations 

```
    python3 manage.py runserver makemigrations 
    python3 manage.py migrate 
```

### To Run the Server in your local environment 

` python3 manage.py runserver `

### To login into django admin create superuser
you can click on home on homepage to login or you can type ' http://127.0.0.1:8000/admin '

` python3 manage.py  createsuperuser `


## Homepage Api
API to get department-wise all Employees in Dashboard in the admin panel with Filter Option Department Wise.

URL http://127.0.0.1:8000/


## Main URL For APIS 
URL http://127.0.0.1:8000/api


### Register Api
To Register the new User

URL http://127.0.0.1:8000/api/register


### Login Api
To login the already registered user. Here token is generated for the login user to access the other apis

URL http://127.0.0.1:8000/api/login


### Logout Api
To logout the user

URL - http://127.0.0.1:8000/api/logout


### User-details Api
To get all the details of the user which is logged in

URL -http://127.0.0.1:8000/api/user





