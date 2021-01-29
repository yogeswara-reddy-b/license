# license
SDK license application

1.The first thing to do is to clone the repository:

$ git clone https://github.com/yogeswara-reddy-b/license.git

$ cd Licenseportalapplication

2.Create a virtual environment to install dependencies in and activate it.

3. Then install the dependencies:

(env)$ pip install -r requirements.txt


Walkthrough:

Firstly go though the models created in models.py file. Both Client and License models are cascaded through foreign key. 

after creating the models do the migrations

$ python manage.py makemigrations
$ python manage.py migrate
 
 Check the models representation in migrations file.
 
-- Register the models in the admin.py file
-- 

-- Install djangorestframework by using this command

$ pip install djangorestframework

-- import serializers from DRF and models from models.py file
-- 
serialiazers conversts objects into Json Format

**Create Serializers for client and license

we need the three serailzers for getting cliet data, for sending emails and license 

-- As each serializer requires Meta data which consists model name and fields.
--

--After completing serializers create views for GET request, POST request and for Email mechanism.
--
-- import serializers from serializers.py file and models from models.py file
 from rest framework import status, APIview and response
run the following command for datetime

$ pip install python-dateutil

and also import smtp library which is simple mail transfer protocol for mail extensions.
Implementing the API's
-- go through the GET api
--

1. write a query to get the list of clients and assign to new object
2. returning the respose 

-- POST request 
--
1. assign a new object after the valid details
2. checking the validation through is_valid() method
3. If it is valid, the response will be posted or it will raise the error

-- Email Notification
--
 1. import smtp module
 2. create a function with post request
 3. write a query to get the client details
 4. Then iterate over each client in the list
 5. checkig the conditons with if statement 
 6. if any of the following statements is true then sending a message with corresponding details mentioned in the requirement.
 7. If it is successfull get response "200_OK"
 
-- Register the app in Settings.py file loaction "INSTALLED_APPS"
 --
 and configure the email host details 
EMAIL_BACKEND, 
EMAIL_HOST, 
EMAIL_HOST_USER, 
EMAIL_HOST_PASSWORD, 
EMAIL_PORT, 
EMAIL_USE_TLS, 
EMAIL_USE_SSL.

**Configuring the urls in urls.py file through importing the respective urls and paths.


-- Testing the Application
--

 Run the following command

(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/admin/ with credentials (username = yogeswar, password=123456789)

we can add new client details there and also change the admin_point_of_contact 



**Install the "POSTMAN" for checking the API's

1. GET Api

First run the command

$ python manage.py runserver

place the url http://127.0.0.1:8000/clients-license/ in path then click send
you will get the list of clients with details

2. Post APi
 
change the request type from get to post
place the url http://127.0.0.1:8000/create-license/ in path and mention the details the body in json format
with package name, licence type and client after click the send button. 
you can see below the details of Post request is created.

3. Email notification

It is POST request only
place the url http://127.0.0.1:8000/send-email/ in path and click on the send button, A mail triggered to client with corressponding details. 
you can see the status "200_ok" below.

**If you want to check the corresponding mail is triggered or not change the admin_point_of contact mail to your mail id and enable less secure app access functionality in your security of google account. 



 
 
 
 


 
 
 
 
 
