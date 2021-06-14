from django.urls import path
from . import views
#from .views import RatesView

app_name = "labs_app"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index),
    #path('comms/', RatesView.as_view()),
]