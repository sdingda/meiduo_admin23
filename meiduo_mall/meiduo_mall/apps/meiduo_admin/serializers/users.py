from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """user's ser"""

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email')