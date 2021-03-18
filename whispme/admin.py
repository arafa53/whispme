from django.contrib import admin
from .models import Contact, PostComment
from.models import Post,Image

# Register your models here.
admin.site.register((Contact,Post,PostComment,Image))

