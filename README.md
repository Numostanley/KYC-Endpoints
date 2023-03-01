This project is a simple KYC endpoint to register and login a user.

The following instructions are to enable you run the project;

First cd into the project root directory.

Next, to run the project from a virtual environment, run the following commands;

```
#install venv python package
python -m venv venv

# activate the virtual environment on windows
.\venv\Scripts\activate

# activate the virtual environment on linux
source venv/bin/activate
```

Next, installing the dependencies with the following command;

```
pip install -r requirements.txt
```

Then start the developement server with the following command;

```
python manage.py runserver
```

The endpoint to register a user is;

```
# Request method: POST
127.0.0.1:8000/register
```

After registering the user, you can log in by first getting an access token from the following url;

```
# Request method: POST
127.0.0.1:8000/api/login/
```

Next, you can access the user data through the following endpoint;

```
# Request method: GET
127.0.0.1:8000/get-details
```

Note: you will need to add the access token gotten from the login endpoint to the request header in order to autenticate the user. You can use the following format in your request header;

```
Authorization: Bearer <access token>
```
