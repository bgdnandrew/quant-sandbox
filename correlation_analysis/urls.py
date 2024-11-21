from django.urls import path
from .views import CorrelationAnalysisView

app_name = "correlation_analysis"

urlpatterns = [
    path(
        "correlation-analysis/",
        CorrelationAnalysisView.as_view(),
        name="correlation-analysis",
    ),
]
