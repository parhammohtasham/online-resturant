from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
# Create your models here.
class Category (models.Model):
    STATUS={
        ("published","Published"),
        ("not-show","Not-Show")
    }
    title=models.CharField(_("عنوان دسته بندی"), max_length=50)
    image=models.ImageField(_("تصویر دسته بندی"), upload_to="categories-images/")
    status=models.CharField(_("وضعیت نمایش"), max_length=10 , choices=STATUS , default="not-show")

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی غذاها")

    def __str__(self):
        return self.title


class Food(models.Model):
    STATUS={
        ("published","Published"),
        ("not-show","Not-Show")
    }
    name=models.CharField(_("نام غذا"), max_length=100)
    descriptions=models.TextField(_("توضیحات"))
    image=models.ImageField(_("تصویر عکس"), upload_to="foods-images/")
    price=models.PositiveBigIntegerField(_("قیمت"),blank=True , null=True)
    category=models.ForeignKey("Category", verbose_name=_("دسته بندی"), on_delete=models.CASCADE , related_name="foods")
    status=models.CharField(_("وضعیت نمایش"), max_length=10 , choices=STATUS , default="not-show" )

    class Meta:
        verbose_name = _("غذاها ")
        verbose_name_plural = _("لیست غذاها")

    def __str__(self) -> str:
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse("food_detail", kwargs={"pk": self.pk})
    