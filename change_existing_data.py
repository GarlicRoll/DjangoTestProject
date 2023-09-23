import datetime
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'djangoProject.settings')  # Replace 'my_project' with your actual project name
django.setup()

from django.contrib.auth.models import User

from main.models import Product, Lesson, LessonView, ProductAccess

lesson1 = Lesson(title="Math", video_url="https://www.youtube.com/results?search_query=math", duration=100)
lesson2 = Lesson(title="Physics", video_url="https://www.youtube.com/results?search_query=physics", duration=1000)

lesson1.save()
lesson2.save()

# Retrieve all users from the database
users = User.objects.all()

print("Users")
# Print details of each user
for user in users:
    print(f'Username: {user.username}, Email: {user.email}, First Name: {user.first_name}, Last Name: {user.last_name}')

# Creating products

product1 = Product(owner=users[2])
product2 = Product(owner=users[2])
product1.save()
product2.save()

# Retrieve all products from the database
products = Product.objects.all()

print("Products")
# Print details of each product
for product in products:
    print(f'Owner: {product.owner.username}, Num of users: {product.users.count()}')

# Retrieve all lessons from the database
lessons = Lesson.objects.all()

print("Lessons")
# Print details of each lesson
for lesson in lessons:
    print(
        f'Title: {lesson.title}, Url: {lesson.video_url}, Duration: {lesson.duration}, Used by {lesson.products.count()} product(s)')

# Adding lessons to the products

lessons[0].products.add(products[0])
lessons[1].products.add(products[0])

# Adding users to products

productAccess1 = ProductAccess(user=users[0], product=products[0])
productAccess2 = ProductAccess(user=users[1], product=products[0])
productAccess1.save()
productAccess2.save()

# Adding views to users

lessonView1 = LessonView(user=users[0], lesson=lessons[0], view_time=70, last_view_date=datetime.date(2023, 9, 20))
lessonView1.save()
lessonView2 = LessonView(user=users[1], lesson=lessons[1], view_time=90, last_view_date=datetime.date(2023, 8, 2))
lessonView2.save()
