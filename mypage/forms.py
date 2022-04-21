from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect


class ChangeProfileForm(forms.Form):
    profile_img = forms.ImageField(
        required=False,
    )
    last_name = forms.CharField(
        required=True,
    )
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(ChangeProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        profile_img = cleaned_data.get("profile_img")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        if email:
            User = get_user_model()
            user = get_object_or_404(User, username=self.user)

            if User.objects.filter(email=email).exists():
                if user.email != email:
                    self.add_error("email", "해당 이메일로 이미 가입하였습니다.")

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')