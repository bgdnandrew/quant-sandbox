from django.db import models


class CorrelationAnalysis(models.Model):
    ticker1 = models.CharField(max_length=10)
    ticker2 = models.CharField(max_length=10)
    correlation = models.FloatField()
    covariance = models.FloatField()
    start_date = models.DateField(help_text="Requested start date for analysis")
    end_date = models.DateField(help_text="Requested end date for analysis")
    first_date = models.DateField(help_text="First date with valid return data")
    last_date = models.DateField(help_text="Last date with valid return data")
    data_points = models.IntegerField(
        help_text="Number of data points used in calculation"
    )
    trading_days = models.IntegerField(
        help_text="Total number of trading days in range"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Correlation Analysis"
        verbose_name_plural = "Correlation Analysis"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Correlation Analysis: {self.ticker1} vs {self.ticker2} ({self.created_at.date()})"
