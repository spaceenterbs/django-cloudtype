from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from django.db.models import F


class Reviews(APIView):
    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = ReviewSerializer(
            all_reviews,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                content = serializer.save()
                return Response(ReviewSerializer(content).data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # 쿠키에서 이미 조회한 비디오의 목록을 가져옴
        review = self.get_object(pk)
        viewed_review = request.COOKIES.get("viewed_videos", "").split(",")
        if str(pk) not in viewed_reviews:
            Review.objects.filter(pk=pk).update(views_count=F("views_count") + 1)
            viewed_reviews.append(str(pk))
        serializer = ReviewSerializer(review)
        response = Response(serializer.data)
        return response

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=HTTP_404_NOT_FOUND)
