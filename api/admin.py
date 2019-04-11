from django.contrib import admin
from .models import VkUser, Post, Media # LoadSession
#from solo.admin import SingletonModelAdmin

class MediaInline(admin.StackedInline):
    model = Media

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'likes')
    inlines = [MediaInline]



class MediaAdmin(admin.ModelAdmin):
    pass

# class LoadSessionAdmin(admin.ModelAdmin):
#     pass

admin.site.register(VkUser)
admin.site.register(Post, PostAdmin)
admin.site.register(Media, MediaAdmin)
# admin.site.register(LoadSession, LoadSessionAdmin)