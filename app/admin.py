from django.contrib import admin
from app.models import Post,Tag,Comments

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
