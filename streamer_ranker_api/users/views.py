# django imports
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# drf imports
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
# local imports
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
def sanity_check(request):

    if request.method == 'GET':
        return Response({'msg': 'success get'})
    elif request.method == 'POST':
        return Response({'msg': 'success post'})

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Creation
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # def get_object(self, pk):
    #     try:
    #         return User.objejcts.get(pk=pk)
    #     except User.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    