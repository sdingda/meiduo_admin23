from rest_framework import serializers

from users.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    """user's ser"""

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'password')
        # id is default read_only

        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
            },
            'username': {
                'max_length': 20,
                'min_length': 5,
            },

        }

    def validate_mobile(self,value):
        if not re.match(r'1[3-9]\d{9}',value):
            raise serializers.ValidationError('error format of mobile num ')
        return value


    def create(self, validated_data):
        """ rewrite the way encrypted the password """
        # user = super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()

        user = User.objects.create_user(**validated_data)
        return user


































































