# Requirements

Create a new `.env` file in the directory and add the required env variables like `SECRET_KEY` and `DEBUG`

# How to run

use
```
python manage.py runserver
```
and navigate to `localhost:8000` to access the application

# Endpoints

| Endpoint | Request Type | Args | Return |
| -------- | -------------| ---- | ------ |
| bank/detail/\<ifsc\> | GET | - | -ifsc -branch -address -city -district -state -bank -name |
| bank/branches/\<name of the bank\>/\<city of the bank\> | GET | - | -ifsc -branch -address -city -district -state -bank -name |