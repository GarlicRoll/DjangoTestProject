import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from main.models import Lesson, Product, User, ProductAccess, LessonView

# Create new example objects using the Django ORM
lesson1 = Lesson(title="Math", video_url="https://www.youtube.com/results?search_query=math", duration=100)
lesson2 = Lesson(title="Physics", video_url="https://www.youtube.com/results?search_query=physics", duration=1000)

lesson1.save()
lesson2.save()

user1 = User(username="Admin", password="Admin")
user2 = User(username="Misha", password="Misha")

user1.save()
user2.save()

product1 = Product(owner=user1)

product1.save()

product1.users.add(user2)

lessonView1 = LessonView(user=user2, lesson=lesson1, view_time=70, viewed=False)

lessonView1.save()