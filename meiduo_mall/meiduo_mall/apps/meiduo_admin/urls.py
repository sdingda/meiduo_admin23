from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import statistical, users

urlpatterns = [
    # 登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
    # 日增用户统计
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 日活跃用户统计
    url(r'^statistical/day_active/$', statistical.UserDayActiveCountView.as_view()),
    # 日下单用户统计
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersCountView.as_view()),
    # 月增用户统计
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 日分类商品访问量统计
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),


    # --------------user manage's router--------------------------------
    url(r'^users/$', users.UserView.as_view()),

]
