from django.contrib import admin

from website.models import Post, Contact

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status')
    list_filter = ('status',)
    ordering = ['-created_date' ]
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)

  
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)