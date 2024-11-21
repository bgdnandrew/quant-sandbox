from rest_framework import serializers
from .models import CorrelationAnalysis


class CorrelationAnalysisRequestSerializer(serializers.Serializer):
    ticker1 = serializers.CharField(max_length=10)
    ticker2 = serializers.CharField(max_length=10)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)


class CorrelationAnalysisResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrelationAnalysis
        fields = "__all__"
