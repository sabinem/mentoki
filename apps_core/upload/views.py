# -*- coding: utf-8 -*-

import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import File, DocFile
from .forms import DocumentForm


@login_required
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocFile(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload:list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = DocFile.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'uploadlist.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


@csrf_exempt
@require_POST
@login_required
def upload_photos(request):
    print "in upload photos"
    images = []
    for f in request.FILES.getlist("file"):
        obj = File.objects.create(upload=f, is_image=True)

        print "object created"
        images.append({"filelink": obj.upload.url})
    print images
    jsondata = json.dumps(images)
    print jsondata
    response = HttpResponse()
    response['Content-Type'] = "text/javascipt"
    json_data = json.dumps(images)
    print json_data
    response.write(json_data)
    print response
    return response


@login_required
def recent_photos(request):
    print "i am here in recent photos"
    images = [
        {"thumb": obj.upload.url, "image": obj.upload.url}
        for obj in File.objects.filter(is_image=True).order_by("-date_created")[:2]
    ]
    response = HttpResponse()
    response['Content-Type'] = "text/javascipt"
    json_data = json.dumps(images)
    print json_data
    response.write(json_data)
    return response
