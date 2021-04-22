from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImagesSerializer, SKUSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser


class ImagesView(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ImagesSerializer
    queryset = SKUImage.objects.all()
    pagination_class = PageNum

    def simple(self, request):
        """get sku goods info """

        # 1.query all sku goods
        skus = SKU.objects.all()
        # 2. return after ser
        ser = SKUSerializer(skus, many=True)
        return Response(ser.data)
