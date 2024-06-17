from django.contrib import admin
from .models import Foods , CategoryMenu , Reser , Clients

admin.site.register(Clients)

admin.site.register(Foods)

admin.site.register(CategoryMenu)

class ReserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'datetime', 'number')
    list_filter = ('user',)


admin.site.register(Reser,ReserAdmin)






