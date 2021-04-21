from datetime import timedelta

from django.utils import timezone

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import GoodsVisitCount
from meiduo_admin.serializers.statistical import GoodsDaySerializer
from users.models import User


class UserCountView(APIView):
    """用户总量统计"""

    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_date = timezone.now()
        # now_date = timezone.now()
        # 获取用户总量
        count = User.objects.all().count()

        # 返回结果
        return Response({
            'date': now_date,
            'count': count,
        })


class UserDayCountView(APIView):
    """日增用户统计"""

    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取今天时间
        now_date = timezone.now()

        # 获取今天零点
        zeroToday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        # 获取明天零点
        zerotomorrow = zeroToday + timezone.timedelta(days=1)

        # 日增用户统计
        count = User.objects.filter(date_joined__gte=zeroToday, date_joined__lt=zerotomorrow).count()

        # 返回结果
        return Response({
            'date': now_date,
            'count': count,

        })


class UserDayActiveCountView(APIView):
    """日活用户统计"""

    # 权限指定
    # permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_date = timezone.now()

        # 获取今天零点
        zeroToday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        # 获取明天零点
        zerotomorrow = zeroToday + timezone.timedelta(days=1)

        # 日活用户统计
        count = User.objects.filter(last_login__gte=zeroToday, last_login__lt=zerotomorrow).count()

        # 返回结果
        return Response({
            'date': now_date,
            'count': count,
        })


class UserDayOrdersCountView(APIView):
    """日下单用户统计"""

    # 权限指定
    # permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_date = timezone.now()

        # 获取今天零点
        zeroToday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        # 获取明天零点
        zerotomorrow = zeroToday + timezone.timedelta(days=1)

        # 下单用户统计
        count = len(set(User.objects.filter(orders__create_time__gte=zeroToday, orders__create_time__lt=zerotomorrow)))

        # 返回结果
        return Response({
            'date': now_date,
            'count': count,
        })


class UserMonthCountView(APIView):
    """月增用户统计"""

    # 指定管理员权限
    # permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = timezone.now()

        # 获取今天零点
        zeroToday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        # 获取明天零点
        zerotomorrow = zeroToday + timezone.timedelta(days=1)

        # 获取一个月前日期的零点
        start_date = zeroToday - timedelta(days=29)
        # 创建空列表保存每天的用户量
        date_list = []

        for i in range(30):
            # 循环遍历获取当天日期零点
            index_date = start_date + timedelta(days=i)
            # 指定下一天日期零点
            next_date = start_date + timedelta(days=i + 1)

            # 查询条件是大于等于当前日期index_date，小于明天日期的用户cur_date，得到当天用户量
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()

            date_list.append({
                'count': count,
                'date': index_date
            })

        return Response(date_list)


class GoodsDayView(APIView):
    """日分类商品访问量"""

    # 权限指定
    # permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_date = timezone.now()

        # 获取今天零点
        zeroToday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        # 获取明天零点
        zerotomorrow = zeroToday + timezone.timedelta(days=1)

        # 日分类商品访问
        goods= GoodsVisitCount.objects.filter(date__gte=zeroToday, date__lt=zerotomorrow)

        # 序列化返回分类数量
        ser = GoodsDaySerializer(goods, many=True)

        return Response(ser.data)
