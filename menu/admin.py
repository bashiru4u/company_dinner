from django.contrib import admin
from django.utils.html import format_html
from .models import Food, Ingredient, Vote

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    # Only these fields will appear on the add/edit form:
    fields = ('name', 'description', 'image')

    list_display = ('name', 'image_thumbnail')
    inlines = [IngredientInline]

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height:auto;"/>',
                obj.image.url
            )
        return '-'
    image_thumbnail.short_description = 'Image'


  

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user','food','timestamp')
