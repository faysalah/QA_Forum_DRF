from django.contrib import admin
from forum.models import Tag, Thread, Answer, Comment, Response
# Register your models here.
admin.site.register(Tag)
admin.site.register(Thread)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Response)