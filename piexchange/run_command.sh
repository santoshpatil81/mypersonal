# create a user with the following creadentials
# username : admin
# password: admin
python manage.py createsuperuser

# Get a list of all users
http -a admin:admin GET http://localhost:8000/users/

# Create two new customers

http -a admin:admin POST http://127.0.0.1:8000/customer/ cust_name="test1" contact_num="12345678912"
http -a admin:admin POST http://127.0.0.1:8000/customer/ cust_name="test2" contact_num="999999999"

# View customer deatils
http -a admin:admin GET http://127.0.0.1:8000/customer/1/ 
http -a admin:admin GET http://127.0.0.1:8000/customer/2/ 

# Search customers based on a portion of contact number
http -a admin:admin GET http://127.0.0.1:8000/search/123/
http -a admin:admin GET http://127.0.0.1:8000/search/999/

# Negative test - No authentication
http GET http://127.0.0.1:8000/search/999/
