from rest_framework.pagination import PageNumberPagination


class StudyPaginator(PageNumberPagination):
    page_size = 10