from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bundle, Doc 
from django.contrib import messages
import json

# Create your views here.


def irigasi(request):
    isfirst = True
    boxlist = []
    docs = Doc.objects.all()
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


        # dt = (doc.bundle.box_number, doc.bundle.bundle_number, doc.doc_number, doc.bundle.code, doc.bundle.title,  
        #       doc.description, doc.bundle.year, doc.doc_count, doc.bundle.orinot)
        # boxlist.append(dt)
    # return HttpResponse(list(json.dumps(boxlist)))

    # boxdict = Bundle.objects.order_by('box_number').values('box_number').distinct()
    # for box in boxdict:
    #     if isfirst:
    #         firstbox = box['box_number']
    #     bundles = Bundle.objects.filter(box_number=box['box_number']).order_by('bundle_number').prefetch_related('docs')
    #     bundlelist = []
    #     for bundle in bundles:
    #         if isfirst:
    #             firstbundle = bundle.bundle_number
    #             isfirst = False
    #         docs = bundle.docs.all().values()
    #         bundledict = {'bundle_number': bundle.bundle_number, 'code': bundle.code, 'title': bundle.title, 'year': bundle.year, 'orinot': bundle.orinot, 'title':bundle.title, 'data': list(docs)}
    #         bundlelist.append(bundledict)
    #     boxlist.append({'box_number': box['box_number'], 'data': bundlelist})    
    # # return HttpResponse(list(json.dumps(boxlist)))
    context = {
        "data": boxlist,
    }
    return render(request=request, template_name='irigasi2.html', context=context)
