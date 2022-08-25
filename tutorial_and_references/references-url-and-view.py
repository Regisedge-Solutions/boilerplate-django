# ######## Table of contents ########
# 1) Main website urls.py 
# 2) Individual app urls.py 
# 3) Individual app views.py 
# 4) Individual app viewsets.py 



######## 1) Main website urls.py ########

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]



######## 2) Individual app urls.py  ########

from django.urls import path

from . import views # views.py is a file the current directory 
from . import viewsets # viewsets.py is a file the current directory 

urlpatterns = [
    path('', views.index, name='index'),
]



urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


######## 3) views.py file  ########

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404 # shortcuts in Django

from .models import Question

# The TEMPLATES settings allows to define how templating should work. By default it looks for a template directory in the app directories
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



######## 4) viewsets.py file  ########