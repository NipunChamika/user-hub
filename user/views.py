from django.shortcuts import render
import pyrebase


config = {
    "apiKey": "AIzaSyD8LKb-1rSspyI1J1S5gh6226niCs4qLrI",
    "authDomain": "user-hub-project.firebaseapp.com",
    "databaseURL": "https://user-hub-project-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "user-hub-project",
    "storageBucket": "user-hub-project.appspot.com",
    "messagingSenderId": "1087560919378",
    "appId": "1:1087560919378:web:eef9b3f627c28ec17bb28b"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()


def index(request):
    return render(request, 'index.html')
