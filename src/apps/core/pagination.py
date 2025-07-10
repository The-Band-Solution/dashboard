from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'current_page': self.page.number,
                'per_page': self.page.paginator.per_page,
                'max_per_page': self.max_page_size,
                'total': self.page.paginator.count
            },
            'data': data
        })
