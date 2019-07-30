import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from booktest.models import BookInfo


class BookListView(View):
    """
    获取所有图书、增加图书
    """
    def get(self, request):
        """
        获取所有的图书数据
        """
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
        新增一个图书数据
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # TODO: 此处详细的校验参数省略

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=book_dict.get('bpub_date')
        )

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }, status=201)

# /books/(?P<pk>\d+)/
class BookDetailView(View):
    """
    获取、修改、删除指定图书
    """
    def get(self, request, pk):
        """
        获取指定图书
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

    def put(self, request, pk):
        """
        修改指定图书
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # TODO: 此处详细的校验参数省略

        book.btitle = book_dict.get('btitle')
        book.bpub_date = book_dict.get('bpub_date')
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

    def delete(self, request, pk):
        """
        删除指定图书：
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)