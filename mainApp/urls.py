from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AddShow.as_view(),name='addandshow'),
    path('edit/<int:id>/',views.UserUpdateView.as_view(),name="edit"),
    path('delete/<int:id>/',views.DeleteView.as_view(),name="delete")
]
