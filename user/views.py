from django.contrib import messages
from django.shortcuts import render, redirect
from requests.exceptions import RequestException
import pyrebase
from .forms import UserForm


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


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f'Form Data: { data }')
            try:
                db.child('users').push(data)
                messages.success(request, 'User created successfully!')
                return redirect('index')
            except RequestException as e:
                print(f'Error pushing data to firebase: { e }')
                messages.error(
                    request, 'Error connecting to the database. Try again later.')
    else:
        form = UserForm()

    return render(request, 'user_form.html')
