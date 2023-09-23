from django.urls import path
from . import views


urlpatterns = [
    path('user/lessons/', views.UserLessonList.as_view(), name='user-lesson-list'),
    path('user/products/<int:product_id>/lessons/', views.UserProductLessonList.as_view(),
         name='user-product-lesson-list'),
    path('products/statistics/', views.ProductStatistics.as_view(), name='product-statistics'),


    path('auth/token/', views.CustomObtainAuthToken.as_view(), name='get-auth-token'),
    path('auth/register/', views.UserRegistrationView.as_view(), name='register'),
]