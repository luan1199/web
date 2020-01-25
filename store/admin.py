from django.contrib import admin

from .models import Post
# Register your models here.

# tornando o modelo post visível na pagina de admin.
admin.site.register(Post)
