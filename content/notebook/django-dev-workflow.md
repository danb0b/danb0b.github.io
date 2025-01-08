---
title: Django Development Workflow
weight: 99
tags: 
- python
- django
summary: " "
---

Derived from [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)

```bash
cd websites
django-admin startproject murdermystery
cd murdermystery
python3 manage.py runserver
```

hit ctrl+c to stop

Create a new script builder app

```bash
python3 manage.py startapp scriptbuilder
nano murdermystery/settings.py
```

See this [section](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) to pre-define a custom user class before creating any databases.

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'script_builder.apps.ScriptBuilderConfig'
]
```

Update Database if necessary.

```bash
TIME_ZONE = 'UTC'
```

```bash
TIME_ZONE = 'America/Phoenix'
```


Edit URL mappings

nano murdermystery/urls.py 

add to bottom 

```
# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('script_builder/', include('script_builder.urls')),
]
```

```
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

save and close

----

Now paste the following into 

```bash
nano script_builder/urls.py
```

```bash
from django.urls import path
from . import views

urlpatterns = [

]
```


```bash
python manage.py makemigrations
python manage.py migrate
```


```bash
python manage.py runserver
```

## Models

Add models according to [this page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)

## Register models and add super user

```bash
nano script_builder/admin.py
```

```bash
from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
```

```bash
python manage.py createsuperuser
python3 manage.py runserver
```

Go to <localhost:8000/admin>