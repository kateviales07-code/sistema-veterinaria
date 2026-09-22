from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MascotaPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'pagina_actual': self.page.number,
            'total_paginas': self.page.paginator.num_pages,
            'total_mascotas': self.page.paginator.count,
            'resultados': data
        })