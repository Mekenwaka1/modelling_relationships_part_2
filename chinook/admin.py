from django.contrib import admin
from chinook.models import Artist, Album, MediaType, Genre, Track, Playlist     

# Register your models here
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(MediaType)
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Playlist)
