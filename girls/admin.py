from django.contrib import admin
from girls.models import Girls, Gifts, Wishes


class GirlsAdmin(admin.ModelAdmin):
    list_display = ('fio', 'flour', 'code')
    readonly_fields = ('code',)


class GiftsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class WishesAdmin(admin.ModelAdmin):
    list_display = ('girl', 'flour', 'gift', 'status', 'time_seconds')
    list_editable = ('status',)
    list_filter = ('gift', 'status')
    search_fields = ('girl__fio',)

    def has_add_permission(self, request):
        return False

    def time_seconds(self, obj):
        return obj.date.strftime("%H:%M")

    def flour(self, obj):
        return obj.girl.flour


admin.site.register(Girls, GirlsAdmin)
admin.site.register(Gifts, GiftsAdmin)
admin.site.register(Wishes, WishesAdmin)
