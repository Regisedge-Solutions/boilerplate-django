# The ideal directory structure for Django projects

* Template references
* The project folder 
* How to create the project folder 
* Decision on best structuring for apis

## Template references 
https://github.com/cookiecutter/cookiecutter-django

## The project folder 

.gitignore 
.dockerignore 
.env
env.example 
env/
Dockerfile
requirements.txt 
manage.py 
docs/
static/
media/
templates/
tests/
project_name/
    __init__.py 
    settings.py 
    urls.py 
    wsgi.py 
    asgi.py
apps/
    app1/
        migrations/
            __init__.py 
        templates/
        __init__.py 
        admin.py
        models.py
        views.py
        viewsets.py
        services.py 
        selectors.py 
        serializers.py 
        api.py
utils/
    utils1.py 
    utils1.py 


Notes:- 
1) Some programmers break settings.py and requirements.txt into multiple files
e.g. 
instead of 
`settings.py `
have the following 
```
settings/   
    __init__.py
    base.py 
    production.py 
    staging.py 
    development.py
```

or
instead of 
`requirements.txt` 
have the following 
```
requirements/
    base.txt 
    production.txt 
    staging.txt
    development.txt
```

## How to create the directory structure

* Make the folder
```
mkdir <project_folder>
cd <project_folder>
```

* Setup virtual environment
```
python -m venv env 
source env/bin/activate
python -m pip install --upgrade pip 
pip install django 
```

* Setup the django project
```
django-admin startproject <project_name> . 
mkdir static media templates 
```
```
# Make changes to settings.py 

    # Enter at the end of the file
        # Static files (CSS, JavaScript, Images)
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

        # Media Files
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = '/media/'


    # Add the new folder to the templates
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/',],
        'APP_DIRS': True,

```
```
python manage.py collectstatic
```

* Setup the first app 
```
mkdir apps
cd apps
djando-admin startapp <app_name> 
djando-admin startapp app1 
Make changes to settings.py 

# Make changes to the settings.py to include this app 
    # Add the following to INSTALLED_APPS
        'apps.app1', # <--- here
```

* Setup Docker 
```
Add env folder to dockerignore
Add DS_Store folder to dockerignore (for all subdirectories)
Create the Dockerfile for creating images 
Create the docker-compose file for creating the complete application stack 
```

* Setup git 
```
Add env folder to gitignore
Add DS_Store folder to gitignore (for all subdirectories)
```

* Setup requirements
```
pip freeze > requirements.txt 
pip install -r requirements.txt 
```


## Decision on best structuring for apis

(Should be able to support versioning of apis)
* Option 1: Create a separate api app and import models into this app (Preferred)
* Option 2: Add viewsets and api files in the existing apps in the project (for small usecases)
https://stackoverflow.com/questions/14269719/django-rest-framework-api-versioning

