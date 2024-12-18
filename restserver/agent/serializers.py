import re
from rest_framework import serializers
from .models import Agent
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.utils.timezone import now

# Custom Email Backend for authentication
class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

# Email validation function
def is_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None


class RegisterAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('This field may not be blank', code='authorization')
        elif Agent.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('Entered Email already registered', code='authorization')
        return value
    
    def create(self, validated_data):
        user = Agent.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Both email and password are required.')

        return data

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class ForgotPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not Agent.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account is associated with this email.")
        return value


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            agent = Agent.objects.get(reset_password_token=data['token'])
            if agent.reset_password_expiration < now():
                raise serializers.ValidationError("The token has expired.")
            return data
        except Agent.DoesNotExist:
            raise serializers.ValidationError("Invalid reset token.")