from __future__ import unicode_literals
from django.contrib import admin
# import from this app
from .models import Forum, SubForum, Thread, Post


class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'courseevent', 'id',  )
    list_filter = ( 'courseevent', )
    list_display_links =  ('courseevent','title')


class SubForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'forum', 'display_nr', )
    list_filter = ( 'forum', )


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('modified', 'id', 'forum','title', 'subforum')
    list_filter = ( 'forum' , 'subforum', 'author')
    list_display_links  = ('subforum', 'forum')
    readonly_fields = ('modified', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('modified',  'id', 'thread', 'author', 'created')
    list_filter = ( 'thread__subforum',  'author' )


admin.site.register(Forum, ForumAdmin)
admin.site.register(SubForum, SubForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)