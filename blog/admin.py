from django.contrib import admin

from .models import Post, PostFile

class PostFileInlineAdmin(admin.TabularInline):
    model = PostFile
    fields = ('file',)
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user' ,'title', 'is_active', 'is_public', 'created_time')
    inlines = (PostFileInlineAdmin, )


@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    pass