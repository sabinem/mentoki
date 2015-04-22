from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import RequestContext
from.forms import LoginForm


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_page = reverse('desk:start')
            else:
                next_page = reverse('userauth:login')
                messages.error(request, "Ihr Account wurde deaktiviert. Bitte nehmen Sie Kontakt zu uns auf, wenn Sie Ihnen wieder aktivieren wollen.")
        else:
            next_page = reverse('userauth:login')
            messages.error(request, u'Ung\u00FCltiges Login')
    else:
        return render_to_response('login.html',  context_instance=RequestContext(request))

    return HttpResponseRedirect(next_page)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    next_page =  '/'
    return HttpResponseRedirect(next_page)







