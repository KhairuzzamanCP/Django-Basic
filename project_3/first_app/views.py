from django.shortcuts import render
import datetime

# Create your views here.

def home(resuest):
    d = {'author': 'Rahim' , 'age': 5, 'list': ['python','is','best'], 'brithday':datetime.datetime.now(),'val':'','courses': [
        
        {
          'id' : 1,
          'name' : 'Python',
          'fee' : 5000
        },
        {
          'id' : 2,
          'name' : 'Django',
          'fee' : 10000
        },
        {
          'id' : 3,
          'name' : 'C',
          'fee' : 5000
        }
    ]}
    return render (resuest, 'home.html' ,d)