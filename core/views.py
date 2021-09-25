from django.http import HttpResponse
from django.shortcuts import render
from core.forms import CoreForm
from core.models import Core

def home(request):
    ctx = {}
    if request.method == 'GET':
        form = CoreForm()
        posts = Core.objects.all()
        ctx['posts'] = posts
        ctx['form'] = form
    else:
        form = CoreForm(request.POST)
        ctx['form'] = form
        if form.is_valid:
            form.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("data save failed")
    return render(request, 'post.html', ctx)