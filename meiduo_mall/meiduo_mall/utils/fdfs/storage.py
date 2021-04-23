import os

from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import get_tracker_conf, Fdfs_client


class FdfsStorage(Storage):
    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        pass

    def url(self, name):
        return settings.FDFS_BASE_URL + name

# from settings.dev import FASTDFS_PATH
#
#
# class FdfsStorage(Storage):
#     """自定义文件存储系统，修改存储的方案"""
#
#     def __init__(self, fdfs_base_url=None):
#         """
#         构造方法，可以不带参数，也可以携带参数
#         :param base_url: Storage的IP
#         """
#         self.fdfs_base_url = fdfs_base_url or settings.FDFS_BASE_URL
#         #self.FASTDFS_PATH = FASTDFS_PATH
#
#     def _open(self, name, mode='rb'):
#         pass
#
#     def _save(self, name, content):
#         pass
#
#
#     def url(self, name):
#         """
#         返回name所指文件的绝对URL
#         :param name: 要读取文件的引用:group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg
#         :return: http://192.168.103.158:8888/group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg
#         """
#         # return 'http://192.168.103.158:8888/' + name
#         # return 'http://image.meiduo.site:8888/' + name
#         return self.fdfs_base_url + name
