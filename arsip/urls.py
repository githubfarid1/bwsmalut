from django.urls import path
from .views import irigasi, pdf_view, airbaku

urlpatterns = [
    path(route='irigasi', view=irigasi, name="irigasi"),
    path(route='airbaku', view=airbaku, name="airbaku"),
    path(route='pdf_view', view=pdf_view, name="pdf_view"),


]