from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "username","password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "User with this email does not exist."}
            )

        if user.check_password(password):
            attrs["username"] = user.username
        else:
            raise serializers.ValidationError({"password": "Invalid password."})

        return super().validate(attrs)
