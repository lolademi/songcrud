from django.contrib import admin
from . models import Artiste
from . models import Song
from . models import Lyrics

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)


