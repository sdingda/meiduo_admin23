from rest_framework import serializers

from goods.models import SKU, GoodsCategory


class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model=SKU
        fields='__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=GoodsCategory
        fields='__all__'









