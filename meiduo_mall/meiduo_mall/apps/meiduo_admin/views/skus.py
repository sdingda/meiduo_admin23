from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU, GoodsCategory
from meiduo_admin.serializers.skus import SKUSerializer, GoodsCategorySerializer
from meiduo_admin.utils import PageNum


class SKUView(ModelViewSet):
    # define ser
    serializer_class = SKUSerializer
    # define queryset
    queryset = SKU.objects.all()
    # define paginator
    pagination_class = PageNum
    # define permission
    permission_classes = [IsAdminUser]


    @action(methods=['get'], detail=False)
    def categories(self, request):
        """
        get goods category of 3 degree
        :param request:
        :return:
        """
        data = GoodsCategory.objects.filter(subs__id=None)
        ser = GoodsCategorySerializer(data, many=True)

        return Response(ser.data)
