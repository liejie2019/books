# import os
#
#
# from django.test import TestCase
#
# # Create your tests here.
# class User(object):
#     def __init__(self,username,age):
#         self.username=username
#         self.age = age
#
#
# from rest_framework import  serializers
#
#
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     age = serializers.IntegerField()
#
#
# # if __name__ == '__main__':
# #     user = User('itcast',13)
# #     serializers = UserSerializer(user)
# #
# #     res = serializers.data
# #     print(res)
#
#
# if __name__ == '__main__':
#     req_data = {'username':'itheima','age':6}
#
#     serializers = UserSerializer(data= req_data)
#     res = serializers.is_valid()
#     print(res)
#     res_errors = serializers.errors
#     print(res_errors)
#
#     res_data = serializers.validated_data
#     print(res_data)
#
#
#
