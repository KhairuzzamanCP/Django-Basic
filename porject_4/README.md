<!-- Project Over View -->

## Working with Static Files inside Project

# Static file Global

### **at first Static floder create and img uploded**

### then settings.py and Now create Declare with STATICFILES_DIRS list

### **Example**

### STATICFILES_DIRS = [

    BASE_DIR/'static',

]

### then template floder create and html file create any name

### then settings.py and TEMPLATES Declare with DIRS list

### **Exapmle**

### TEMPLATES = [

    'DIRS': ['templates'],

]

---

## Working with Static Files inside App

### **django app create commmad**

```django
django-admin startapp first_app
```

### then create file urls.py

### settings.py Declare with app installed list

### **Example**

### INSTALLED_APPS = [

    'first_app',

]

### then project floder urls include

### **Example**

```
from django.urls import path , include
urlpatterns = [
   path('first/', include('first_app.urls')),
]
```
