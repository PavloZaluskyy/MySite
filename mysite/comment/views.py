from django.shortcuts import render
from .models import *
from .forms import *


def landing(request):
    form = CommentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    comments = Comment.objects.filter()
    return render(request, 'index.html', locals())