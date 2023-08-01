from django.contrib import admin
from .models import *
# from .models import Costume

# class CostumeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'is_available')
#     list_filter = ('category', 'is_available')
#     search_fields = ('name', 'description')
#     prepopulated_fields = {'slug': ('name',)}
#     ordering = ('name',)
#     actions = ['make_available', 'make_unavailable']

#     def make_available(self, request, queryset):
#         queryset.update(is_available=True)
#         self.message_user(request, "Selected costumes have been made available.")

#     make_available.short_description = "Mark selected costumes as available"

#     def make_unavailable(self, request, queryset):
#         queryset.update(is_available=False)
#         self.message_user(request, "Selected costumes have been made unavailable.")

#     make_unavailable.short_description = "Mark selected costumes as unavailable"

# admin.site.register(Costume, CostumeAdmin)

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductImage)
# admin.site.register(Users)
# admin.site.register(Profile)