from django.contrib import admin
from core.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

# @admin.register(Destinations)
# class DestinationsAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Post)
# class CommentAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Post)
# class VoteAdmin(admin.ModelAdmin):
#     pass