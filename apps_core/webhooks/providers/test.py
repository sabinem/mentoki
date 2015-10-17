import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


#Using Django
@csrf_exempt
def my_webhook_view(request):
    # Retrieve the request's body and parse it as JSON
    print "_______________________"
    print request.body
    print "_____________________"
    #event_json = json.load(request.body)
    # Do something with event_json

    return HttpResponse(status=201)
