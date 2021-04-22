from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SPUSpecification
from meiduo_admin.serializers.specs import SpecsSerializer, SPUSerializer
from meiduo_admin.utils import PageNum
from goods.models import SPU


class SpecsView(ModelViewSet):
    """the size of goods of add, delete, get, modify """
    # define the queryset
    queryset = SPUSpecification.objects.all()
    # define the ser
    serializer_class = SpecsSerializer

    pagination_class = PageNum

    def simple(self, request):
        """
        get SPU_goods info
        :param request:
        :return:
        """
        spus = SPU.objects.all()
        ser = SPUSerializer(spus, many=True)

        return Response(ser.data)
