from django import forms
from bbuser.models import User


class ProfileForm(forms.Form):
    profile_img = forms.ImageField(
        required=False,
    )
    last_name = forms.CharField(
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        profile_img = cleaned_data.get("profile_img")
        last_name = cleaned_data.get("last_name")
