import mutagen
from django.conf import settings
from fdfs_client.client import get_tracker_conf, Fdfs_client
from rest_framework import serializers

from goods.models import SKUImage, SKU
from celery_tasks.static_file.tasks import get_detail_html

class ImagesSerializer(serializers.ModelSerializer):
    """
        图片序列化器
    """

    # sku_id = serializers.IntegerField()

    class Meta:
        model = SKUImage
        fields = "__all__"

    def create(self, validated_data):

        # 3. build fastdfs client

        FASTDFS_PATH = get_tracker_conf(settings.FASTDFS_PATH)

        client = Fdfs_client(FASTDFS_PATH)

        # get the object of request
        request = self.context['request']

        file = request.FILES.get('image')

        # 4. upload image
        res = client.upload_appender_by_buffer(file.read())

        # 5. judge whether upload success
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError({'error': '图片上传失败'})

        # 6. save images table

        img = SKUImage.objects.create(sku=validated_data['sku'], image=res['Remote file_id'].decode())

        # async task generate detail html

        get_detail_html.delay(img.sku.id)

        return img



    def update(self, instance, validated_data):

        # 3. build fastdfs client

        FASTDFS_PATH = get_tracker_conf(settings.FASTDFS_PATH)

        client = Fdfs_client(FASTDFS_PATH)

        # get the object of request
        request = self.context['request']

        file = request.FILES.get('image')

        # 4. upload image
        res = client.upload_appender_by_buffer(file.read())

        # 5. judge whether upload success
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError({'error': '图片上传失败'})

        # 6. update images table

        instance.image=res['Remote file_id'].decode()
        instance.save()
        get_detail_html.delay(instance.sku.id)

        return instance



class SKUSerializer(serializers.ModelSerializer):
    """
    sku ser
    """

    class Meta:
        model = SKU
        fields = ('id', 'name')


















































