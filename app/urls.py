from django.urls import path
from .views import *

urlpatterns = [
    # ...

  path('',home_incio, name="home_incio")

]

