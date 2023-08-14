from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from .models import Bigreview
from .serializers import BigreviewSerializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from django.db.models import F
from datetime import datetime, timedelta


class Bigreviews(APIView):
    def get(self, request, pk):
        bigreviews = Bigreview.objects.all()
        serializer = BigreviewSerializer(bigreviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = BigreviewSerializer(data=request.data)
            if serializer.is_valid():
                content = serializer.save()
                return Response(
                    BigreviewSerializer(content).data, status=HTTP_201_CREATED
                )
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


# class BigreviewDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Bigreview.objects.get(pk=pk)
#         except Bigreview.DoesNotExist:
#             return Response(status=HTTP_404_NOT_FOUND)


# class BigreviewDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Bigreview.objects.get(pk=pk)
#         except Bigreview.DoesNotExist:
#             return Response(status=HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         bigreview = self.get_object(pk)
#         viewed_bigreviews = request.COOKIES.get("viewed_videos", "").split(",")
#         if str(pk) not in viewed_bigreviews:
#             Youtube_Video.objects.filter(pk=pk).update(views_count=F("views_count") + 1)
#             viewed_videos.append(str(pk))
#         serializer = Youtube_VideoSerializer(youtube_video)
#         response = Response(serializer.data)
#         return response

#     def put(self, request, pk):
#         youtube_video = self.get_object(pk)
#         serializer = Youtube_VideoSerializer(youtube_video, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         youtube_video = self.get_object(pk)
#         youtube_video.delete()
#         return Response(status=HTTP_404_NOT_FOUND)
