from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
import re
from django.core.validators import validate_email

#def _validate_email(email):
#    try:
#        validate_email(email)
#    except ValidationError as e:
#        print("bad email1, details:", e)
#    else:
#        print("good email1")


def validate_postnums(postId):
    if str(postId).isdigit() == False:
        raise ValidationError(
            ('%(postId)s is not a number'),
            params={'value': postId},
        )


class Comment(models.Model):
    email = models.CharField(max_length=200, validators=[validate_email])
    name = models.CharField(max_length=150)
    postId = models.IntegerField(validators=[validate_postnums])
    body = models.TextField()
    id_com = models.IntegerField()


    def __str__(self):
        return self.name




