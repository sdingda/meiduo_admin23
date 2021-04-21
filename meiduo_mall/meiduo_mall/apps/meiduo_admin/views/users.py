from rest_framework.generics import ListAPIView
from meiduo_admin.serializers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class UserView(ListAPIView):
    """get user info"""

    # define queryset
    queryset = User.objects.all()
    # define ser
    serializer_class = UserSerializer
    # use the paginator
    pagination_class = PageNum


