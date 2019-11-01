from django.contrib import admin
from web.models import GuessNumbers
from web.models import Post
from web.models import Event

# Register your models here.
admin.site.register(GuessNumbers)
admin.site.register(Post)
admin.site.register(Event)