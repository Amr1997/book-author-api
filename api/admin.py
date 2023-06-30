from django.contrib import admin
from .models import Author, Book, Page, CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name',  'last_name')
    
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')

    def first_name(self, obj):
        return obj.user.first_name

    first_name.short_description = 'First Name'

    def last_name(self, obj):
        return obj.user.last_name

    last_name.short_description = 'Last Name'

    def email(self, obj):
        return obj.user.email

    email.short_description = 'Email'


class PageInline(admin.TabularInline):
    model = Page
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'brief' , 'image')
    list_filter = ('author',)
    search_fields = ('title', 'author__user__username')
    inlines = [PageInline]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('book',  'content')
    list_filter = ('book',)
    search_fields = ('book__title', 'content')
    
    
    