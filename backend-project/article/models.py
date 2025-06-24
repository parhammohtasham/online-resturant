from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    title=models.CharField(_("عنوان"), max_length=50)
    summary=models.CharField(_("خلاصه"), max_length=200)
    content=models.TextField(_("محتوا"))
    created=models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(_("زمان بروزرسانی"), auto_now=True, auto_now_add=False)
    image=models.ImageField(_("تصویر مفاله"), upload_to="article_images/",default="static/images/profile.jpg")
    author=models.ForeignKey(get_user_model(), verbose_name=_("نویسنده"), on_delete=models.CASCADE, related_name="articles")
    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقالات")

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse("Article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article=models.ForeignKey("Article", verbose_name=_("عنوان مقاله"), on_delete=models.CASCADE)
    comment=models.TextField(_("نظر"))
    writer=models.ForeignKey(get_user_model(), verbose_name=_("نویسنده نظر"), on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name=_("نظر")
        verbose_name_plural=_("نظرات")

    def __str__(self):
        return f"{self.writer}"
    
