from ckeditor.fields import RichTextField
from django.db import models



# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=32,verbose_name="Başlık")
    content = RichTextField()
    image = models.FileField(blank = True,null = True,verbose_name="Resim Ekle")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    
    class Meta():
        ordering = ["-created_date"]



class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=("Makale"),on_delete=models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_author_image_url = models.CharField(blank=True, null=True,max_length=800)
    comment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment_content

    class Meta():
        ordering = ["-comment_date"]
    