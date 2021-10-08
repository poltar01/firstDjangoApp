from django.db import models
from django import forms

# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE,verbose_name="Kullanıcı Adı",related_name="userinfo")

    username = models.CharField(blank = True,null = True,verbose_name="Kullanıcı Adı",max_length=50)
    profile_image = models.FileField(verbose_name="Pofil Fotoğrafı Ekle",upload_to="profile_pics",default='/profile_pics/default.jpg')
    full_name = models.CharField(blank = True,null = True,verbose_name="Ad Soyad",max_length=50)
    email_address = models.EmailField(blank = True,null = True,verbose_name="e-Posta Adresi")
    birth_date = models.DateField(blank = True,null = True,verbose_name="Doğum Tarihi (GG/AA/YY)")



    def __str__(self):
        return self.user.username + " - User Informations"

