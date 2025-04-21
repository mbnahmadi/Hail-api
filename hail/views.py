from django.shortcuts import render
from .utils import read_latest_csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import ValidationError
from pathlib import Path


class GetHailDataView(APIView):
    # permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('station_name', openapi.IN_QUERY, description="نام ایستگاه", type=openapi.TYPE_STRING, required=True),
        ])
    def get(self, request):
        try:
            station_name = request.query_params.get('station_name')
        except:
            raise ValidationError("پارامتر station_name ضروری است") 
        data_folder = f'./data_folder/{station_name}/'
        if not Path(data_folder).exists() or not Path(data_folder).is_dir():  
            return Response({'error': 'نقطه ای با این نام یافت نشد'}, status=status.HTTP_404_NOT_FOUND) 
        data = read_latest_csv(data_folder)
        return Response({"station_name":station_name,"data": data})

