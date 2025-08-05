from django.urls import path
# from .views import CourseListAPIView, CourseDetailAPIView,     CourseListCreateAPI, CourseRetrieveUpdateDestroyAPI,  CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, FilteredCourseList
from .views import FilteredCourseList

urlpatterns = [
    # APIView
    # path('courses/', CourseListAPIView.as_view(), name='course-list'),
    # path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # GenericAPIView + Mixins
    # path('courses/', CourseListCreateAPI.as_view(), name='mixins-course-list-create'),
    # path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPI.as_view(), name='mixins-course-detail-update-delete'),
    
    # path('courses/', CourseListCreateAPIView.as_view(), name='generic-course-list'),
    # path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='generic-course-detail'),

    path('filter/', FilteredCourseList.as_view(), name='filter_courses'),
]