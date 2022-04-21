from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CheckPasswordForm
from django.contrib.auth import logout
from django.contrib import messages


@login_required
def profile(request):
    return render(request, 'mypage/profile.html')

@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/accounts/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'mypage/profile_delete.html', {'password_form':password_form})
