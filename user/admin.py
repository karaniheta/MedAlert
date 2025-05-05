from django.contrib import admin
from .models import HealthTip, FirstAidCondition, FirstAidSection

class FirstAidSectionInline(admin.TabularInline):
    model = FirstAidSection
    extra = 1

@admin.register(FirstAidCondition)
class FirstAidConditionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    inlines = [FirstAidSectionInline]

@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'importance_level', 'created_at']
    search_fields = ['title', 'summary', 'category']

