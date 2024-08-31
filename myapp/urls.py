from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, UserTypeViewSet, PatientViewSet, DiseaseViewSet, VisitScheduleViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'users', UserTypeViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'diseases', DiseaseViewSet)
router.register(r'visit-schedules', VisitScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
