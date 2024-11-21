from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import (
    CorrelationAnalysisRequestSerializer,
    CorrelationAnalysisResponseSerializer,
)
from .models import CorrelationAnalysis
from algorithms.correlation import CorrelationCalculator


class CorrelationAnalysisView(APIView):
    """
    API View for performing correlation analysis between two stocks.
    """

    def post(self, request):
        request_serializer = CorrelationAnalysisRequestSerializer(data=request.data)
        if not request_serializer.is_valid():
            return Response(
                request_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validated_data = request_serializer.validated_data
            result = CorrelationCalculator.calculate(
                ticker1=validated_data["ticker1"],
                ticker2=validated_data["ticker2"],
                start_date=validated_data.get("start_date"),
                end_date=validated_data.get("end_date"),
            )

            # convert string dates to datetime.date objects
            result["first_date"] = datetime.strptime(
                result["first_date"], "%Y-%m-%d"
            ).date()
            result["last_date"] = datetime.strptime(
                result["last_date"], "%Y-%m-%d"
            ).date()

            # create model instance with only the fields that match our model
            model_fields = [f.name for f in CorrelationAnalysis._meta.fields]
            filtered_result = {k: v for k, v in result.items() if k in model_fields}

            analysis = CorrelationAnalysis.objects.create(**filtered_result)
            response_serializer = CorrelationAnalysisResponseSerializer(analysis)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
