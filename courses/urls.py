from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, EnrollmentViewSet, QuizViewSet, health_check

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('', include(router.urls)),
]