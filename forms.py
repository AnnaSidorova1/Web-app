from django.db.models import fields
from .models import Comment
from django.forms import ModelForm, widgets, TextInput, Textarea


class CommentForm(ModelForm):

    class Meta: 
        model = Comment
        fields = ["email", "name", "postId", "body", "id_com"]
        widgets = {
            "email": TextInput(attrs={
                'style': "width: 40%",
                'placeholder': "Введите ваш email",
                'class': "form-control",
                'required': 'Укажите email'
            }),
            "name": TextInput(attrs={
                'style': "width: 40%",
                'placeholder': "Введите заголовок",
                'class': "form-control"
            }),
            "postId": TextInput(attrs={
                'style': "width: 40%",
                'placeholder': "Введите номер поста",
                'class': "form-control",
                'required': 'Укажите номер поста'
            }),
            "body": Textarea(attrs={
                'style': "width: 40%",
                'placeholder': "Введите текст комментария",
                'class': "form-control",
                'required': 'Укажите текст комментария'
            }),
            "id_com": TextInput(attrs={
                'style': "width: 40%",                
                'class': "form-control",     
                'default':0,
                'value': Comment.objects.count()+1,
                'editable':False
            }),
        }
