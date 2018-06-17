# SIGNUP

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


# LOGIN

curl -X POST \
  http://127.0.0.1:5000/login \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "johndoe",
	"password": "654321"
}'


# LOGOUT

curl -X GET http://127.0.0.1:5000/logout


# MY BALANCE

curl -X GET \
  http://127.0.0.1:5000/my_balance \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "kevin92dev",
	"password": "123456"
}'


# TRANSFER

curl -X POST \
  http://127.0.0.1:5000/transfer \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "johndoe",
	"amount": 100
}'