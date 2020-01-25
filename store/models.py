from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# classes post com parametro models.Model, significa que post é de django.
# e será salvo no banco de dados. # herança


class Post(models.Model):

    # atributo autor
    # ForeignKey: link para outro modelo
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)# definição de texto limitado com 200 caracteres

    text = models.TextField()# campo para texto sem limite fixo.

    created_date = models.DateTimeField(default=timezone.now) # modelo de data e hora atual.

    published_date = models.DateTimeField(blank=True, null=True) # 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title