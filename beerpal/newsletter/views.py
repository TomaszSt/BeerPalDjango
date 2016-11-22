from django.shortcuts import render
from django.template import context

from .forms import SignUpForm
# Create your views here.

def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=True)
        if not instance.full_name:
            instance.full_name = "Tomasz"
        instance.save()

    context = {
        "form": form
    }
    return render(request,"home.html",context)

def signup(request):
    return render(request,"home.html",{})