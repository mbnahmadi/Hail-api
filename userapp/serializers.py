# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password

# User = get_user_model()

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

#     class Meta:
#         model = User
#         fields = ('username', 'password')

#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError("این نام کاربری قبلاً استفاده شده است.")
#         return value

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

# class APIKeySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('api_key',) 