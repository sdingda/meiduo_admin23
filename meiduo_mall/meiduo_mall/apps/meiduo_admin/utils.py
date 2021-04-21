from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'id': user.id
    }


# custom defined one paginator

class PageNum(PageNumberPagination):
    page_size_query_param = 'pagesize'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            "counts": self.page.paginator.count,
            "lists": data,
            "page": self.page.number,
            "pages": self.page.paginator.num_pages,
            "pagesize": self.max_page_size
        })

        # OrderedDict([
        # ('count', self.page.paginator.count),
        # ('next', self.get_next_link()),
        # ('previous', self.get_previous_link()),
        # ('results', data)
