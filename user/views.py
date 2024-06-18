import os
from django.contrib import messages
from django.shortcuts import render, redirect
from requests.exceptions import RequestException
from dotenv import load_dotenv
import pyrebase
from .forms import UserForm

load_dotenv()

config = {
    "apiKey": os.getenv('apiKey'),
    "authDomain": os.getenv('authDomain'),
    "databaseURL": os.getenv('databaseURL'),
    "projectId": os.getenv('projectId'),
    "storageBucket": os.getenv('storageBucket'),
    "messagingSenderId": os.getenv('messagingSenderId'),
    "appId": os.getenv('appId')
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()


def user_list(request):
    users = db.child('users').get().val()
    if users is None:
        users = {}
    return render(request, 'user_list.html', {'users': users.items()})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                db.child('users').push(data)
                messages.success(request, 'User created successfully!')
                return redirect('user_list')
            except RequestException as e:
                print(f'Error pushing data to firebase: { e }')
                messages.error(
                    request, 'Error connecting to the database. Try again later.')
    else:
        form = UserForm()

    return render(request, 'user_create.html')


def user_update(request, user_id):
    user = db.child('users').child(user_id).get().val()
    print(user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                db.child('users').child(user_id).update(data)
                messages.success(request, 'User updated successfully!')
                return redirect('user_list')
            except RequestException:
                messages.error(
                    request, 'Error connecting to the database. Try again later.')
    else:
        form = UserForm(initial=user)
    return render(request, 'user_update.html', {'form': form})


def user_delete(request, user_id):
    user = db.child('users').child(user_id)

    if not user:
        messages.error(request, 'Incorrect user!')

    try:
        user.remove()
        messages.success(request, 'User deleted successfully!')
    except RequestException:
        messages.error(request, 'Error deleting user. Try again later.')

    return redirect('user_list')
