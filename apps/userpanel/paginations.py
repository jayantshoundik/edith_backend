from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

'''
Custom Zatchup paginations Paginations 
'''
class SwooshPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size =100

    def get_paginated_response(self, data):
        limit = self.request.query_params.get('page_size', 5)
        return Response({
            'status': True,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size':int(limit),
            'results': data
        })