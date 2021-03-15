from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Type1,Type2,Type3,Type4,Type
from .serializers import Type1Serializer, Type2Serializer, Type3Serializer, Type4Serializer, TypeSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import status
# Create your views here.
class Type1View(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types=Type1.objects.all()
        Types_serializer = Type1Serializer(Types, many=True)
        return Response(Types_serializer.data)
class Type2View(APIView):

    """

    all Type2

    """

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):

        Types=Type2.objects.all()

        Types_serializer = Type2Serializer(Types, many=True)

        return Response(Types_serializer.data)

class Type3View(APIView):

    """

    all Type3

    """

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):

        Types=Type3.objects.all()

        Types_serializer = Type3Serializer(Types, many=True)

        return Response(Types_serializer.data)

class Type4View(APIView):

    """

    all Type4

    """

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):

        Types=Type4.objects.all()

        Types_serializer = Type4Serializer(Types, many=True)

        return Response(Types_serializer.data)

# class TypeView(APIView):
#     def get(self, request, format=None):
#         Types = Type.objects.all()
#         Types_serializer = TypeSerializer(Types, many=True)
#
#         return Response(Types_serializer.data)
#
#     def post(self, request):
#
#         name = request.data.get('name')
#
#         category_type = int(request.data.get('lei'))
#
#         parent_category_id = request.data.get('parent')
#
#         type = Type()
#
#         type.name = name
#
#         type.category_type = category_type
#
#         if parent_category_id:
#             parent_category = Type.objects.filter(id=parent_category_id).first()
#
#             type.parent_category = parent_category
#
#         type.save()
#
#         type_serializer = TypeSerializer(type)
#
#         return Response(type_serializer.data)


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    @action(methods=["get"], detail=False, url_name="get_type")
    def get_data(self, request, *args, **kwargs):
        print("hello world")
        return Response(status=status.HTTP_200_OK)

    @action(methods=["put"], detail=False, url_name="put_type")
    def put_data(self, request, *args, **kwargs):
        print("hello world")
        return Response(status=status.HTTP_200_OK)
