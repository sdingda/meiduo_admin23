from rest_framework import serializers
from goods.models import SKUImage, SKU


class ImagesSerializer(serializers.ModelSerializer):
    """
        图片序列化器
    """
    sku_id = serializers.IntegerField()

    class Meta:
        model = SKUImage
        fields = "__all__"


class SKUSerializer(serializers.ModelSerializer):
    """
    sku ser
    """
    class Meta:
        model = SKU
        fields = ('id', 'name')
