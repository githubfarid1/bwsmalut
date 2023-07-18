from django.urls import path
from .views import irigasi

urlpatterns = [
    path(route='irigasi', view=irigasi, name="irigasi"),

]