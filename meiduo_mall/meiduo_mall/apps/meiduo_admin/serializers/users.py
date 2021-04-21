from rest_framework import serializers

from users.models import User


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

    def create(self, validated_data):
        """ rewrite the way encrypted the password """
        # user = super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()

        user = User.objects.create_user(**validated_data)
        return user


































































