
from django.utils import timezone



class ZeroToday(object):
    def zday(self):
        """获取今天零点"""
        now_date = timezone.now()
        zerotoday = now_date - timezone.timedelta(hours=now_date.hour,
                                                  minutes=now_date.minute,
                                                  seconds=now_date.second,
                                                  microseconds=now_date.microsecond)
        return zerotoday

    def tomz(self):
        """获取明天零点"""
        tomz = self.zday()
        return tomz


if __name__ == '__main__':
    a = ZeroToday()
    print(a.zday())
    print(a.tomz())

# # 获取前一天的当前时间
# yesterdayNow = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
# # 获取明天的当前时间
# tomorrowNow = now + datetime.timedelta(hours=23, minutes=59, seconds=59)
#
# print('时间差', datetime.timedelta(hours=23, minutes=59, seconds=59))
# print('当前时间', now)
# print('今天零点', zeroToday)
# print('获取23:59:59', lastToday)
# print('昨天当前时间', yesterdayNow)
# print('明天当前时间', tomorrowNow)
# 输出：
# 时间差 23:59:59
#
# 当前时间 2019-08-19 10:16:32.510070
# 今天零点 2019-08-19 00:00:00
#
# 获取23:59:59 2019-08-19 23:59:59
# 昨天当前时间 2019-08-18 10:16:33.510070
# 明天当前时间 2019-08-20 10:16:31.510070
