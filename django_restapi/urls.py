from django.contrib import admin
from django.urls import path
from api import views
from deserial import views as deView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>/', views.student_details),
    path('stulist/', views.StudentAPI.as_view()),
    path('productData/', deView.product_data),
]
