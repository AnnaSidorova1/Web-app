from django.http import HttpResponse
import json
from labs_app.forms import CommentForm
import urllib.request
import requests
from django.shortcuts import get_object_or_404, render, redirect
from .models import Comment
from django.core.validators import validate_email
from django.views.generic import DetailView


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
    if Comment.objects.count() < 500:
        load_data()
    data = Comment.objects.order_by('postId').all()
    return render(request, 'labs_app/index.html', {'home': 'Домашняя страница', 'comms': data })


def about(request):
    error = ''
    if request.method == 'POST':
        form_1 = CommentForm(request.POST)
        if form_1.is_valid() :
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


def gen_com(request, prod):
    category = request.GET.get("com", "")
    output = "<h2> Product № {0}  Category: {1} </h2>".format(prod, category)
    return HttpResponse(output)
    data = category
    return render(request, 'labs_app/test_generate.html', {'gener': 'Сгенерированная страница', 'coms': data})
    #return HttpResponse(output)


def show_post(request, id_c):
    post = get_object_or_404(Comment, id_com=id_c)

    context = {
        'post': post,
        'title' : post.name,
        'selected_p': post.id_com,
    }

    return render(request, 'labs_app/test_generate.html', context=context)


#class CommentsDetailView(DetailView):
#    model = Comment
#    template_name = 'labs_app/test_generate.html'
#    pk_url_kwarg = 'id_com'
#    context_object_name = 'comment'

#    def get_object(self):
#        return get_object_or_404(Comment, id_com=self.request.user.id)


class ResultsView(DetailView):
    model = Comment
    template_name = 'labs_app/test_generate.html'
    context_object_name = 'comment'
    slug_field = 'id_com'
    slug_url_kwarg = 'slug'
