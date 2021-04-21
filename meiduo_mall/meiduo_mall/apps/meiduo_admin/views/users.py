from rest_framework.generics import ListCreateAPIView
from meiduo_admin.serializers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class UserView(ListCreateAPIView):
    """get user info"""

    # define queryset
    queryset = User.objects.all()
    # define ser
    serializer_class = UserSerializer
    # use the paginator
    pagination_class = PageNum

    # rewrite the way of get queryset
    def get_queryset(self):
        if self.request.query_params.get('keyword') == '':
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=self.request.query_params.get('keyword'))
# vague query:  username__contains=
