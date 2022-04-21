from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from mypage.forms import ChangeProfileForm
from django.contrib.auth import get_user_model


@login_required
def profile(request):
    return render(request, "mypage/profile.html")


@login_required
def ChangeProfileView(request):
    if request.method == "POST":
        form = ChangeProfileForm(request.POST, request.FILES, user=request.user)
        User = get_user_model()
        user = get_object_or_404(User, username=request.user)
        if form.is_valid():
            if user.profile_img:
                user.profile_img.delete()
                user.save()
            user.profile_img = form.cleaned_data["profile_img"]
            user.last_name = form.cleaned_data["last_name"]
            input_email = form.cleaned_data["email"]

            user.save()
            return redirect("/")
        else:
            return render(
                request,
                "mypage/change_profile.html",
                {"form": form, "user": user},
            )
    form = ChangeProfileForm()
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    print(user)
    return render(request, "mypage/change_profile.html", {"form": form, "user": user})
