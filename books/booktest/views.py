from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializers


class BookInfoViewSet(ModelViewSet):
    """视图集"""

    query_set = BookInfo.objects.all()
    serializers_class = BookInfoSerializers

















