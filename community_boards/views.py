from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from django.db.models import F
from datetime import datetime, timedelta


class Boards(APIView):
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = BoardSerializer(data=request.data)
            if serializer.is_valid():
                content = serializer.save()
                return Response(BoardSerializer(content).data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class BoardDetail(APIView):
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        board = self.get_object(pk)
        board.delete()
        return Response(status=HTTP_404_NOT_FOUND)

        # 쿠키에서 이미 조회한 비디오의 목록을 가져옴

    #     board = self.get_object(pk)
    #     viewed_boards = request.COOKIES.get("viewed_videos", "").split(",")
    #     if str(pk) not in viewed_boards:
    #         Board.objects.filter(pk=pk).update(views_count=F("views_count") + 1)
    #         viewed_boards.append(str(pk))
    #     serializer = BoardSerializer(board)
    #     response = Response(serializer.data)

    #     # 쿠키 설정
    #     expires = datetime.strftime(
    #         datetime.utcnow() + timedelta(days=30), "%a, %d-%b-%Y %H:%M:%S GMT"
    #     )
    #     response.set_cookie(
    #         "viewed_videos",
    #         ",".join(viewed_boards),
    #         expires=expires,
    #         httponly=True,
    #         secure=True,
    #         samesite="Lax",
    #     )

    #     return response
    #     # return Response(serializer.data)

    # def put(self, request, pk):
    #     board = self.get_object(pk)
    #     serializer = BoardSerializer(board, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def delete(self, request, pk):
    #     board = self.get_object(pk)
    #     board.delete()
    #     return Response(status=HTTP_404_NOT_FOUND)
