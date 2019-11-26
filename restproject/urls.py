
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.PersonListAPIView.as_view()),
    path('apicreate/', views.PersonCreateAPIView.as_view()),
    path('api/<int:pk>/', views.PeopleRetrieveAPIView.as_view()),
    path('apiupdate/<int:pk>/', views.PersonUpdateAPIView.as_view()),
    path('apidelete/<int:pk>/', views.PersonDestroyAPIView.as_view()),
]
