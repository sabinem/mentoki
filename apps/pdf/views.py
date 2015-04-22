from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import ImageUploadForm
from .models import Image

class ImageView(FormView):
    template_name = 'main/image_form.html'
    form_class = ImageUploadForm

    def form_valid(self, form):
        profile_image = Image(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk': self.id})

class ImageDetailView(DetailView):
    model = Image
    template_name = 'pdf/upload_image.html'
    context_object_name = 'image'


class ImageIndexView(ListView):
    model = Image
    template_name = 'pdf/image_view.html'
    context_object_name = 'images'
    queryset = Image.objects.all()


import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from .models import File


@csrf_exempt
@require_POST
@login_required
def upload_photos(request):
    images = []
    for f in request.FILES.getlist("file"):
        obj = File.objects.create(upload=f, is_image=True)
        images.append({"filelink": obj.upload.url})
    return HttpResponse(json.dumps(images), mimetype="application/json")


@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.upload.url, "image": obj.upload.url}
        for obj in File.objects.filter(is_image=True).order_by("-date_created")[:20]
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")