import json
from labs_app.forms import CommentForm
import urllib.request
import requests
from django.shortcuts import render, redirect
from .models import Comment
from django.core.exceptions import ValidationError
from django.core import validators
import re
from django.core.validators import validate_email

# def contact(request):
#   return HttpResponse("<h2>Контакты</h2>")
#Comment.id_com = Comment.objects.count()
#print(Comment.id_com) 


def load_data():
    response = json.loads(requests.get("https://jsonplaceholder.typicode.com/comments")._content)
    for r in response:
        com = Comment()
        com.email = r["email"]
        com.name = r["name"]
        com.postId = r["postId"]
        com.body = r["body"]
        com.id_com = r["id"]
        com.save()

def index(request):
    #Comment.objects.all().delete()
    if Comment.objects.count() == 0:
        load_data()
    data = Comment.objects.order_by('postId').all()
    return render(request, 'labs_app/index.html', {'home': 'Домашняя страница', 'comms': data })


def _validate_email(email):
    try:
        re.findall(r"[\w\.-]+@[\w\.-]+(\.[\w]+)+", email)
    except ValidationError as e:
        print("bad email222, details:", e)
        return False
    else:
        print("good email222")
        return True
    #try : re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', email)
    #except ValidationError:
    #    return False


def about(request):
    error = ''
    if request.method == 'POST':
        form_1 = CommentForm(request.POST)
        if form_1.is_valid() & _validate_email(form_1["email"]):
            form_1.save()
            return redirect('home')
        else:
            error = 'Неверные данные'
    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'labs_app/add-comms.html', context)


def feat(request):
    return render(request, 'labs_app/features.html')
