from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Count, Sum
from django.contrib.auth.models import User
from .models import Product, ProductAccess, Lesson, LessonView
from .serializers import UserSerializer, ProductSerializer, ProductAccessSerializer, LessonSerializer, \
    LessonViewSerializer, UserRegistrationSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
'''Implement an API for displaying a list of all lessons for all products that the user has access to, 
with information about the status and viewing time.'''


class UserLessonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        product_ids = request.user.accessible_products.values_list("id", flat=True)
        lessons = Lesson.objects.filter(products__id__in=product_ids)
        lesson_views = LessonView.objects.filter(user=request.user, lesson__in=lessons)
        serializer = LessonViewSerializer(lesson_views, many=True)
        return Response(serializer.data, status=200)


'''Implement an API with displaying a list of lessons for a specific product to which the user has access, 
with displaying information about the status and viewing time, as well as the date of the last viewing of the video.'''


class UserProductLessonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_id):
        if request.user.accessible_products.filter(id=product_id).exists():
            lessons = Lesson.objects.filter(products__id=product_id)
            lesson_views = LessonView.objects.filter(user=request.user, lesson__in=lessons)
            serializer = LessonViewSerializer(lesson_views, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({"detail": "Forbidden"}, status=403)


'''Implement an API for displaying product statistics. It is necessary to display a list of all products on the 
platform, attach information to each product: The number of lessons viewed from all students. How much time did all 
the students spend watching the videos in total? The number of students engaged in the product. The percentage of 
product purchase (calculated based on the number of accesses to the product divided by the total number of users on 
the platform).'''


class ProductStatistics(APIView):
    def get(self, request):
        products = Product.objects.all()
        user_count = User.objects.count()
        data = []

        for product in products:
            lessons_viewed = LessonView.objects.filter(viewed=True, lesson__products=product).count()
            total_view_time = LessonView.objects.filter(lesson__products=product).aggregate(Sum('view_time'))[
                'view_time__sum']
            students = product.users.count()
            purchase_percentage = (students / user_count) * 100

            data.append({
                "product_id": product.id,
                "lessons_viewed": lessons_viewed,
                "total_view_time": total_view_time,
                "students": students,
                "purchase_percentage": purchase_percentage
            })

        return Response(data, status=200)


# Auth
class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = UserSerializer(token.user, context={'request': request})
        return Response({
            'token': token.key,
            'user': user.data
        })


'''Users can authenticate themselves using the /api/auth/token/ endpoint by sending their username and password to 
obtain a token. They can then use this token in the 'Authorization' header for requests to other API endpoints:'''


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to register.
