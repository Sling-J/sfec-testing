from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, groups, students, test, answers


urlpatterns = [
   path('', home, name='home_url'),
   path('groups/', groups, name='groups_url'),
   path('<str:slug>/students/', students, name='students_url'),
   path('test/', test, name='test_url'),
   path('answers/', answers, name='answers_url')
]

if settings.DEBUG == True:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)