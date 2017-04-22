from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return "Коментар %s " % (self.name)

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'Коментарі'

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)