from django.db import models
from django.utils.text import slugify


class FieldsModel(models.Model):


    label = models.CharField(max_length=800)
    slug = models.SlugField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(FieldsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
        db_table = "fields"

    def __str__(self):
        return self.label
