from django.contrib import admin
from .models import CorrelationAnalysis


@admin.register(CorrelationAnalysis)
class CorrelationAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "ticker1",
        "ticker2",
        "correlation",
        "covariance",
        "start_date",
        "end_date",
        "created_at",
    )
    list_filter = ("created_at", "start_date", "end_date")
    search_fields = ("ticker1", "ticker2")
    date_hierarchy = "created_at"
