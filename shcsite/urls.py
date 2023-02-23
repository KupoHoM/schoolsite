from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Lessons.views import LessonsViewSet
from Teachers.views import TeachersViewSet
from Discipline.views import DisciplineViewSet
from Homework.views import HomeWorkViewSet
from django.views.generic import TemplateView
from templates.views import Register

app_name = 'myapp'

schema_view = get_swagger_view(title='DRF API')
router = routers.DefaultRouter()
router.register(r'Discipline', DisciplineViewSet,)
router.register(r'Lessons', LessonsViewSet)
router.register(r'Teachers', TeachersViewSet)
router.register(r'HomeWork', HomeWorkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view,),

    path('api/v1/', include(router.urls)),


    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('register/', Register.as_view(), name='register'),

]
