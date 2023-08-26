from .models import *
from .serializers import *
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.
class BoardList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CreateBoardSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get_board(self, pk):
        board = get_object_or_404(Board, pk = pk)
        return board
    
    def get(self, request, pk):
        board = self.get_board(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        board = self.get_board(pk)
        serializer = BoardSerializer(board, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        board = self.get_board(pk)
        board.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class CommentList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_comment(self, pk):
        comments = Comment.objects.filter(post__pk = pk)
        return comments
    
    def get(self, request, pk):
        comments = self.get_comment(pk)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, pk):
        board = Board.objects.get(pk = pk)
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user, post = board)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class UnivBoardList(APIView):
    def get(self, request, univ):
        boards = Board.objects.filter(user__university__contains = univ)
        serializer = BoardSerializer(boards, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)