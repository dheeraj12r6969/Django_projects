## URL to be used to access home page

[This text links to app](http://127.0.0.1:8000/admin/).

---
* * *
___

## Run the app using:

1. cd \myblogproject
2. python manage.py runserver

## credentials to use: 

```
username : dheeraj
email: dashora.dheeraj@gmail.com
pass: qwerty120

```

```
Access the Django Admin Site:

Go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier. Here, you can manage users, blog posts, and user profiles.

Access the API Documentation:

If you've included DRF-YASG in your project, you can access the API documentation at http://127.0.0.1:8000/swagger/ or http://127.0.0.1:8000/redoc/.

Testing Authentication and Authorization:

You can test user authentication by obtaining a JWT token. Use a tool like httpie or curl to make requests. For example:

bash
Copy code
http post http://127.0.0.1:8000/api/token/ username=<your_username> password=<your_password>
This will return an access token and a refresh token. You can use the access token to make authenticated requests.

Remember to replace <your_username> and <your_password> with your superuser credentials.

Feel free to explore the API using the Django admin site, API endpoints, and the provided 
```