from django.conf import settings
from fdfs_client.client import Fdfs_client, get_tracker_conf
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImagesSerializer, SKUSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser


#  Fdfs_client 重难点
#  FASTDFS_PATH = get_tracker_conf(settings.FASTDFS_PATH)
#  client = Fdfs_client(FASTDFS_PATH)
#  image=res['Remote file_id'].decode()


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

    # def create(self, request, *args, **kwargs):
    #
    #     # 1. get request data
    #     data = request.data
    #
    #     # 2. validate
    #     ser = self.get_serializer(data=data)
    #     ser.is_valid()
    #     ser.save()
    #     # return Response({
    #     #     'id': img.id,
    #     #     'sku': img.sku_id,
    #     #     'image': img.image.url,
    #     #
    #     # })
    #     return Response(ser.data, status=201)
