from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from meiduo_admin.views import statistical, users, specs, images

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

    # --------------size spu_id 's router--------------------------------
    url(r'^goods/simple/$', specs.SpecsView.as_view({'get': 'simple'})),

    # --------------iamge sku_id 's router--------------------------------
    url(r'^skus/simple/$', images.ImagesView.as_view({'get': 'simple'})),

]
# --------------size table's router--------------------------------

router = DefaultRouter()
router.register('goods/specs', specs.SpecsView, basename='specs')
# print(router.urls)

urlpatterns += router.urls

# -------图片表路由------
router = DefaultRouter()
router.register('skus/images', images.ImagesView, basename='images')
# print(router.urls)
urlpatterns += router.urls





























































