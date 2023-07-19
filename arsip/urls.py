from django.urls import path
from .views import irigasi, pdf_view, search

urlpatterns = [
    path(route='irigasi', view=irigasi, name="irigasi"),
    path(route='pdf_view', view=pdf_view, name="pdf_view"),
    path(route='search', view=search, name="search"),


]