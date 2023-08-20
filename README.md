# MyChat
Based on a YouTube tutorial by [Divanov11](https://www.youtube.com/watch?v=Oxnz8Us1QAQ)

## Description 
A Group video calling application using the Agora Web SDK with a Django backend.

##  How to use this source code

#### 1 - Clone repo
```
git clone https://github.com/Lukebot19/videoChatWebsite
```

#### 2 - Install requirements
```
cd mychat
pip install -r requirements.txt
```
#### 3 - Create a .env file
This app uses environment variables, in the file create the following variables:
```
APP_ID=
APP_CERTIFICATE=
```

#### 4 - Update Agora credentials
In order to use this project you will need to replace the agora credentials in `views.py` and `streams.js`.

Create an account at agora.io and create an `app`. Once you create your app, you will want to copy the `appid` & `appCertificate` to update `.env`.

#### 4 - Start server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

