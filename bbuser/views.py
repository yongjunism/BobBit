from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from datetime import datetime

from django.contrib.auth.decorators import login_required

from .forms import ProfileForm

# Create your views here.


@login_required
def RegisterProfileView(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        User = get_user_model()
        user = get_object_or_404(User, username=request.user)
        if form.is_valid():
            print(request.user)
            if user.profile_img:
                user.profile_img.delete()
                user.save()
            user.profile_img = form.cleaned_data["profile_img"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            return redirect("/user/pointup")
        else:
            return render(
                request,
                "user/register_profile.html",
                {"form": form, "user": user},
            )
    form = ProfileForm()
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    return render(request, "user/register_profile.html",
                  {"form": form, "user": user})


def pointUp(request):
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)

    user.first_login = 0
    user.save()

    if user.last_login2:
        if user.last_login2.day != datetime.today().day:
            user.point = user.point + 100
            user.first_login = 1
            user.last_login2 = datetime.today()
            user.save()
            return redirect("/")
    else:
        user.point = user.point + 100
        user.first_login = 1

    user.last_login2 = datetime.today()
    user.save()

    return redirect("/")
