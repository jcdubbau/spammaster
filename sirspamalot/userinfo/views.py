from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import SpamMessage, Profile
from .forms import SpamMessageForm, UserRegistrationForm
def spam_posted(request):
    Spam = SpamMessage.objects.all()
    context = {
         "Spam": Spam,
    }
    return render(request, "userinfo/spam_posted.html", context) 
     

def registered(request):

    Spam = SpamMessage.objects.all()

    context = {
        "Spam": Spam,

    }

    return render(request, "userinfo/registered.html", context)


def index(request):

    Spam = SpamMessage.objects.all()

    context = {
        "Spam": Spam,

    }

    return render(request, "userinfo/index.html", context)


def index(request):

    Spam = SpamMessage.objects.all()

    context = {
        "Spam": Spam,

    }

    return render(request, "userinfo/index.html", context)

def users_list(request):

    user_list = User.objects.all()

    context = {
        "user_list": user_list,
    }

    return render(request, "userinfo/user_list.html", context)

def user_page(request, id):
    spammer = get_object_or_404(User, pk=id)
    spam = spammer.spammessage_set.all()

    context = {
		"spam": spam,
		"spammer":spammer,
    }

    return render(request, "userinfo/user_page.html", context)

@login_required
def create_message(request):

    if request.method == "POST":
        form = SpamMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_id = request.user.pk
            new_message.save()
            messages.success(request,"Thanks for posting your Spam via SpamMaster3000")
            return redirect('userinfo:index')
    else:
        form = SpamMessageForm()

    context = {
        "form": form,
    }

    return render(request, "userinfo/create_message.html", context)


def register(request):
    if request.method== "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
              form.save()

        return redirect('userinfo:user_list')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }
    return render(request, "userinfo/registration.html", context)
