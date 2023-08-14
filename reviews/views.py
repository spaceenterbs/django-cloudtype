from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)


class Reviews(APIView):
    pass


#     def post(self, request):
#         try:
#             serializer = ReviewSerializer(data=request.data)
#             if serializer.is_valid():
#                 content = serializer.save()
#             return Response(ReviewSerializer(content).data=HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

#     # def get(self, request, pk):
