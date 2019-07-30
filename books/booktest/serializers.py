from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializers(serializers.Serializer):
    class Meta:
        model = BookInfo
        fields = '__all__'