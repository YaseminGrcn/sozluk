from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import *


class PostInline(admin.TabularInline):
    model = Post
    extras = 1
    readonly_fields = ('created', 'edited')
    fieldsets = (
        (None, {
            'fields': ('author', 'created', 'body', 'edited')
        }),
        ('improment', {
            'classes': ('collapse',),
            'fields': ('ip', 'reported')
        }),
    )


@admin.register(Entry)
class Entry(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'last_updated', 'created', 'post_count')
    readonly_fields = ('last_updated', 'created')
    list_per_page = 25
    inlines = [PostInline]

    def view_on_site(self, obj):
        return reverse('entry', kwargs={'slug': obj.slug, 'id': obj.id})

    def post_count(self, obj):
        return obj.post_set.count()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'entry', 'like_count', 'reported')
    exclude = ('likes', 'dislikes')
    list_per_page = 25
    list_filter = ['reported']
    actions = ['set_unreported']

    def like_count(self, obj):
        p = obj.likes.count()
        n = obj.dislikes.count()
        return p-n

    def view_on_site(self, obj):
        return reverse('post', kwargs={'id': obj.id})

    def set_unreported(self, request, queryset):
        queryset.update(reported=False)

    set_unreported.short_description = "Sikayet"
