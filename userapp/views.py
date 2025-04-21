# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from userapp.serializers import UserRegistrationSerializer, APIKeySerializer
# from django.contrib.auth import get_user_model
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# # Create your views here.

# User = get_user_model()
# class UserRegistrationView(APIView):
#     @swagger_auto_schema(
#         operation_description="ثبت نام کاربر جدید",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=['username', 'password'],
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING),
#             }
#         ),
#         responses={
#             201: "کاربر با موفقیت ثبت نام شد",
#             400: "خطا در داده‌های ورودی"
#         }
#     )
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 "message": "کاربر با موفقیت ثبت نام شد",
#                 "username": user.username,
#                 "api_key": str(user.api_key)
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GetAPIKeyView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token authentication", type=openapi.TYPE_STRING, required=True),
#         ],
#         operation_description="دریافت API Key کاربر",
#         responses={
#             200: openapi.Response(
#                 description="API Key کاربر",
#                 schema=openapi.Schema(
#                     type=openapi.TYPE_OBJECT,
#                     properties={
#                         'api_key': openapi.Schema(type=openapi.TYPE_STRING)
#                     }
#                 )
#             ),
#             401: "عدم احراز هویت"
#         },
#         security=[{'Token': []}]
#     )
#     def get(self, request):
#         serializer = APIKeySerializer(request.user)
#         return Response(serializer.data)

