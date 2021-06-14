from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
import re
from django.core.validators import validate_email




class Comment(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    postId = models.IntegerField()
    body = models.TextField()
    id_com = models.IntegerField()


    def __str__(self):
        return self.name

    def _validate_email(email):
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email1, details:", e)
        else:
            print("good email1")
    #try : re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', email)
    #except ValidationError:
    #    return False



