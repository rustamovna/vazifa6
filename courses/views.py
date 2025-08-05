from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from rest_framework import mixins
from rest_framework.generics import GenericAPIView,  ListAPIView
from django.db.models import Q 
### APIView
# class CourseListAPIView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()

#         search_query = request.GET.get("search")
#         if search_query:
#             courses = courses.filter(
#                 Q(title__icontains=search_query) | Q(description__icontains=search_query)
#             )

#         min_price = request.GET.get("min")
#         max_price = request.GET.get("max")
#         if min_price:
#             courses = courses.filter(price__gt=min_price)
#         if max_price:
#             courses = courses.filter(price__lt=max_price)

#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CourseDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         course = self.get_object(pk)
#         if not course:
#             return Response({'error': 'Topilmadi'}, status=404)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         course = self.get_object(pk)
#         if not course:
#             return Response({'error': 'Topilmadi'}, status=404)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         course = self.get_object(pk)
#         if not course:
#             return Response({'error': 'Topilmadi'}, status=404)
#         course.delete()
#         return Response(status=204)


###GenericAPIView + mixins
# class CourseListCreateAPI(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = CourseSerializer

#     def get_queryset(self):
#         queryset = Course.objects.all()

#         #
#         search = self.request.GET.get('search')
#         if search:
#             queryset = queryset.filter(
#                 Q(title__icontains=search) | Q(description__icontains=search)
#             )

#         min_price = self.request.GET.get('min')
#         max_price = self.request.GET.get('max')
#         if min_price:
#             queryset = queryset.filter(price__gte=min_price)
#         if max_price:
#             queryset = queryset.filter(price__lte=max_price)

#         return queryset

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class CourseRetrieveUpdateDestroyAPI(GenericAPIView,
#                                      mixins.RetrieveModelMixin,
#                                      mixins.UpdateModelMixin,
#                                      mixins.DestroyModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)

#     def put(self, request, pk):
#         return self.update(request, pk=pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)

### GenericApiView mixinsiz
class CourseListCreateAPIView(GenericAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        min_price = self.request.GET.get('min')
        max_price = self.request.GET.get('max')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get(self, request):
        courses = self.get_queryset()
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseRetrieveUpdateDestroyAPIView(GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
