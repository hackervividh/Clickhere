from django.contrib import admin
from .models import Category, Post

# Register your models here.

#for configuartion of category admin

class CategoryAdmin(admin.ModelAdmin):
      list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
      search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):

      list_display = ('title',)
      search_fields = ('title',)
      list_filter = ('category', )
      list_per_page = 56

      class Media:
            js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

