from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        if username:
            user = self.instance
            if User.objects.filter(username=username).exclude(id=user.id).exists():
                raise ValidationError('Username already exists')

        email = attrs.get('email')
        if email:
            email = self.instance
            if User.objects.filter(email = email).exclude(id=user.id).exists():
                raise ValidationError('Email already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])

        user.save()

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)

        if password:
            instance.set_password(password)
        instance.save()

        return instance