# Design

I have chosen the Python Django framework to build my application due to the fact that it simplifies and accelarates web development. Apart from that it has support for MVC framework, has robust security features and is compatible with major operating systems and databases. Also, its open source with a large active community.

I have chose PostgresSQL as my backend mainly because its open source, robust, supports high performance and multitasking and can efficiently store large amounts of data.

# How to execute the project

The following command will build the containers and launch the end-to-end tests
```
docker-compose up -d && docker exec -ti django_piexchange_1 bash "run_command.sh"
```

# Tests and Output

## Test 1: Create customers

```
http -a admin:admin POST http://127.0.0.1:8000/customer/ cust_name="test1" contact_num="12345678912"
```
###Output:
```
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 122
Content-Type: application/json
Date: Tue, 18 Feb 2020 00:57:09 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "contact_num": "12345678912",
    "created": "2020-02-18T11:57:09.047148+11:00",
    "cust_id": 1,
    "cust_name": "test1",
    "owner": "admin"
}
```

## Test 2: View Customer details

```
http -a admin:admin GET http://127.0.0.1:8000/customer/1/ 
```
###Output:
```
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 122
Content-Type: application/json
Date: Tue, 18 Feb 2020 00:57:42 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "contact_num": "12345678912",
    "created": "2020-02-18T11:57:09.047148+11:00",
    "cust_id": 1,
    "cust_name": "test1",
    "owner": "admin"
}
```

## Test3: Search customer using a contact number or a portion of the contact number

```
http -a admin:admin GET http://127.0.0.1:8000/search/123/ 
```
###Output:
```
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 124
Content-Type: application/json
Date: Tue, 18 Feb 2020 00:57:52 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "contact_num": "12345678912",
        "created": "2020-02-18T11:57:09.047148+11:00",
        "cust_id": 1,
        "cust_name": "test1",
        "owner": "admin"
    }
]
```

## Test4: Unauthenticated requests fail
```
http -a admin:admin POST http://127.0.0.1:8000/customer/ cust_name="test1"
```
###Output:
```
HTTP/1.1 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 43
Content-Type: application/json
Date: Tue, 18 Feb 2020 00:56:51 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "contact_num": [
        "This field is required."
    ]
}
```