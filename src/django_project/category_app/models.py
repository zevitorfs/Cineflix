from uuid import uuid4
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
# Create your models here.
