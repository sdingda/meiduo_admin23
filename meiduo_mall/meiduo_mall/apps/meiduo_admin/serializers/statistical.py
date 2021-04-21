from rest_framework import serializers
from goods.models import GoodsVisitCount


class GoodsDaySerializer(serializers.ModelSerializer):
    """日分类商品访问量 序列化器"""

    # 指定返回分类名称
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = GoodsVisitCount
        fields = ('count', 'category')