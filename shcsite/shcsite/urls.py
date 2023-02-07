"""shcsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from Lessons.views import LessonsViewSet
from Teachers.views import TeachersViewSet
from Discipline.views import DisciplineViewSet


schema_view = get_swagger_view(title='DRF API')
router = routers.DefaultRouter()
router.register(r'Discipline', DisciplineViewSet,)
router.register(r'Lessons', LessonsViewSet)
router.register(r'Teachers', TeachersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('api/v1/', include(router.urls)),

    # path('api/v1/Discipline/', DisciplineViewSet.as_view()),
    # path('api/v1/Lessons/', LessonsAPIList.as_view()),
    # path('api/v1/Lessons/<int:pk>/', LessonsAPIUpdate.as_view()),
    # path('api/v1/Lessonsdelete/<int:pk>/', LessonsAPIDestroy.as_view()),
    # path('api/v1/Teachers/', TeachersAPIList.as_view()),
    # path('api/v1/Teachers/<int:pk>/', TeachersAPIUpdate.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
