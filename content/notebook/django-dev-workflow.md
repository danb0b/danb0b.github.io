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

## External Resources

* <https://duckduckgo.com/?t=ffab&q=django+library+tutorial&ia=web>
* <https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Admin_site>
* <https://www.danaukes.com/search/?s=django>
* <https://www.danaukes.com/notebook/django-dev-workflow/>
* <https://github.com/danb0b/django_homepage/settings>
* <https://liferaftlabs.com/blog/7-osint-podcasts-every-analyst-should-follow>
* <https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/>
* <https://www.sprinkledata.com/blogs/postgres-vs-mariadb-a-comprehensive-comparison-of-two-leading-relational-database-systems>
* <https://duckduckgo.com/?t=ffab&q=django+paid+blog&ia=web>
* <https://django-tutorial.dev/articles/monetize-django-site/#gsc.tab=0>
* <https://dev.to/saifeddin1/how-to-make-money-using-django-a-practical-guide-for-developers-1p6e>
* <https://djangocentral.com/building-a-blog-application-with-django/>
* <https://medium.com/django-unleashed/how-i-built-a-custom-blog-platform-using-django-in-10-days-ac1dea43b2b5>
* <https://duckduckgo.com/?t=ffab&q=django+import+blog+posts+from+markdown&ia=web>
* <https://dev.to/guzmanojero/how-i-made-my-django-blog-safe-after-adding-markdown-4lpi>
* <https://duckduckgo.com/?t=ffab&q=djano+based+blog+site+that+uses+markdown+files&ia=web>
* <https://blog.markdowntools.com/posts/django-markdown>
* <https://learndjango.com/tutorials/django-markdown-tutorial>
* <https://medium.com/@farad.dev/creating-a-blogging-platform-with-django-and-markdown-support-7ab16c3947bf>
* <https://duckduckgo.com/?t=ffab&q=django+manage+files&ia=web>
* <https://docs.djangoproject.com/en/5.2/topics/files/>
* <https://duckduckgo.com/?q=how+to+list+images+in+a+directory+django&t=ffab&ia=web>
* <https://stackoverflow.com/questions/23525841/displaying-all-images-from-directory-django>
* <https://github.com/mkdocs/mkdocs/blob/master/LICENSE>
* <https://duckduckgo.com/?t=ffab&q=integrate+django+with+static+site+generator&ia=web>
* <https://stackoverflow.com/questions/5150350/using-a-static-website-generator-for-a-blog-on-a-dynamic-website>
* <https://django-distill.com/>
* <https://render.io/>
* <https://saxix.github.io/django-admin-extra-buttons/howto/>
* <https://www.loopwerk.io/articles/2023/adding-custom-actions-django-admin/>
* <https://django-admin-extra-buttons.readthedocs.io/en/latest/>
* <https://medium.com/@asif-biswas/learn-how-to-add-a-custom-button-to-django-admin-panel-the-easiest-way-c11d5d8781a6>
* <https://hakibenita.com/how-to-add-custom-action-buttons-to-django-admin>
* <https://stackoverflow.com/questions/40760880/add-custom-button-to-django-admin-panel>
* <https://github.com/crccheck/django-object-actions>
* <https://docs.djangoproject.com/en/5.2/ref/contrib/admin/actions/>
* <https://dev.to/rockandnull/effortless-django-model-import-export-from-the-admin-panel-h7p>
* <https://docs.djangoproject.com/en/5.2/ref/contrib/admin/>
