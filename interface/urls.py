from django.contrib import admin
from django.urls import path

from application.views import InterviewApi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/interview', InterviewApi.as_view(), name='interview_api')
]
