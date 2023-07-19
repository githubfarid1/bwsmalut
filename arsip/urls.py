from django.urls import path
from .views import irigasi, pdfdownload, airbaku

urlpatterns = [
    path(route='irigasi', view=irigasi, name="irigasi"),
    path(route='airbaku', view=airbaku, name="airbaku"),
    # path(route='pdf_view', view=pdf_view, name="pdf_view"),
    path(route='pdfdownload/<str:link>/<str:doc_id>', view=pdfdownload, name='pdfdownload')



]