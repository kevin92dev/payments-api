# Instructions

1- Clone this repository: ```git clone https://github.com/kevin92dev/payments-api.git```

2- Install needed dependencies using: ```pip3 install -r requirements.txt```

3- Activate virtualenv: ```source venv/activate```

4- Run Flask server: ```FLASK_APP=infrastructure/app.py flask run```

Now our app is running.


## Example cURL API calls:
### Signup

```
curl -X POST \
  http://127.0.0.1:5000/signup \
  -H 'Content-Type: application/json' \
  -d '{
	"firstname": "John",
	"lastname": "Doe",
	"username": "johndoe",
	"password": "654321",
	"bank_account": {
		"iban": "ES1111111111",
		"balance": 100
	}
}'
```


### Login

```
curl -X POST \
  http://127.0.0.1:5000/login \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "johndoe",
	"password": "654321"
}'
```

### Logout

```
curl -X GET http://127.0.0.1:5000/logout
```

### My balance

```
curl -X GET \
  http://127.0.0.1:5000/my_balance \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "kevin92dev",
	"password": "123456"
}'
```

### Transfer

```
curl -X POST \
  http://127.0.0.1:5000/transfer \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "johndoe",
	"amount": 100
}'
```