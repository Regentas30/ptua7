from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class BooksInline(admin.TabularInline):
    model = Book
    can_delete = False
    extra = 0

    def has_change_permission(self, request, obj=None):
        """Makes all fields read-only immediately."""
        return False


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "display_books")
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    readonly_fields = ('uuid',)
    can_delete = False
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    search_fields = ('uuid', 'book__title', 'book__author__first_name',
                     'book__author__last_name')
    list_editable = ('status', )

    fieldsets = (
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
