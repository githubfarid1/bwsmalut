from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bundle, Doc 
from django.contrib import messages
import json
from django.db.models import Q


def getdata(method, parquery, department_id):
    query = ""
    if method == "GET":
        query = parquery

    isfirst = True
    boxlist = []
    # department_id = 1
    if query == None or query == '':
        docs = Doc.objects.filter(bundle__department_id__exact=department_id)
    else:
        docs = Doc.objects.filter(Q(description__icontains=query)  | Q(bundle__title__icontains=query) | Q(bundle__year__contains=query))
    isfirst = True
    curbox_number = ""
    curbundle_number = ""
    
    for ke, doc in enumerate(docs):
        if isfirst:
            isfirst = False
            curbox_number = doc.bundle.box_number
            boxlist.append({"box_number": doc.bundle.box_number,
                            "bundle_number": doc.bundle.bundle_number,
                            "doc_number": doc.doc_number,
                            "bundle_code": doc.bundle.code,
                            "bundle_title": doc.bundle.title,
                            "bundle_year": doc.bundle.year,
                            "doc_description": doc.description,
                            "doc_count": doc.doc_count,
                            "bundle_orinot": doc.bundle.orinot,
                            "row_number": ke + 1,
                            })
            continue
        if curbox_number == doc.bundle.box_number:
            box_number = ""
        else:
            box_number = doc.bundle.box_number
            curbox_number = doc.bundle.box_number
        if curbundle_number == doc.bundle.bundle_number:
            bundle_number = ""
            bundle_code = ""
            bundle_title = ""
            bundle_year = ""
            bundle_orinot = ""
        else:
            bundle_number = doc.bundle.bundle_number
            curbundle_number = doc.bundle.bundle_number
            bundle_code = doc.bundle.code
            bundle_title = doc.bundle.title
            bundle_year = doc.bundle.year
            bundle_orinot = doc.bundle.orinot
        
        doc_number = doc.doc_number
        doc_description = doc.description
        doc_count = doc.doc_count
        boxlist.append({"box_number": box_number,
                        "bundle_number": bundle_number,
                        "doc_number": doc_number,
                        "bundle_code": bundle_code,
                        "bundle_title": bundle_title,
                        "bundle_year": bundle_year,
                        "doc_description": doc_description,
                        "doc_count": doc_count,
                        "bundle_orinot": bundle_orinot,
                         "row_number": ke + 1,
                        })
        
    isfirst = True
    rowbox = 0
    rowbundle = 0
    boxspan = 1
    bundlespan = 1      
    for ke, box in enumerate(boxlist):
        if isfirst:
            isfirst = False
            rowbox = ke
            rowbundle = ke
            boxspan = 1
            bundlespan = 1      
            continue
        if box['box_number'] == "":
            boxspan += 1
        else:
            boxlist[rowbox]['boxspan'] = boxspan
            boxspan = 1
            rowbox = ke

        if box['bundle_number'] == "":
            bundlespan += 1
        else:
            boxlist[rowbundle]['bundlespan'] = bundlespan
            bundlespan = 1
            rowbundle = ke

    # for last record
    if docs.count() != 0:
        boxlist[rowbox]['boxspan'] = boxspan
        boxlist[rowbundle]['bundlespan'] = bundlespan

    return boxlist

def irigasi(request):
    context = {
        "data": getdata(method=request.method, parquery=request.GET.get("search"), department_id=1),
        "link": "irigasi"
    }
    
    return render(request=request, template_name='irigasi.html', context=context)


def airbaku(request):
    context = {
        "data": getdata(method=request.method, parquery=request.GET.get("search"), department_id=2),
        "link": "airbaku"
    }
    
    return render(request=request, template_name='irigasi.html', context=context)
def pdf_view(request):
    with open('/home/farid/pdf/document.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
    
