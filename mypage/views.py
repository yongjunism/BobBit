from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from mypage.forms import ChangeProfileForm, CheckPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from pricePredict.models import Product, VirtualProduct
from django.forms.models import model_to_dict


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

@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        User = get_user_model()
        user = get_object_or_404(User, username=request.user)
        if user.socialaccount_set.all():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/accounts/login/')
        else:
            password_form = CheckPasswordForm(request.user, request.POST)
        
            if password_form.is_valid():
                request.user.delete()
                logout(request)
                messages.success(request, "회원탈퇴가 완료되었습니다.")
                return redirect('/accounts/login/')        
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'mypage/profile_delete.html', {'password_form':password_form})


@login_required
def product_wishlistView(request):
    user = request.user
    w=user.wish_product.all()
    
    return render(request, 'mypage/wishlist.html', {'w': w})