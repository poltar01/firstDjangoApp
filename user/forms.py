from django import forms
from django.core.exceptions import ValidationError
from .models import userInfo

class LoginForm(forms.Form):
    username = forms.CharField(max_length=24,min_length=8,label="Kullanıcı Adı")
    password = forms.CharField(max_length=24,min_length=8,label="Parola",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=24,min_length=8,label="Kullanıcı Adı")
    password = forms.CharField(max_length=24,min_length=8,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=24,min_length=8,label="Parolayı Doğrula",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise ValidationError("Parola Doğrulanamadı!")
        else:
            values = {
                "username" : username,
                "password" : password
            }
        return values

class userInfoForm(forms.ModelForm):
    
    class Meta:
        model = userInfo
        fields = ["profile_image","full_name","email_address","birth_date"]