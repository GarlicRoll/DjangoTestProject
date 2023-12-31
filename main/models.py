from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Create a product entity. The product must have an owner.
# You need to add an entity to save access to the product for the user.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    users = models.ManyToManyField(User, related_name="accessible_products", through='ProductAccess')

    def __str__(self):
        return f"Product {self.id} owned by {self.owner}"


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_accesses")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="user_accesses")

    def __str__(self):
        return f"Access for {self.user} to {self.product}"


# Create a lesson entity. The lesson can be in several products at the same time.
# The lesson should contain basic information: the title, the link to the video, the duration of viewing (in seconds).
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    duration = models.PositiveIntegerField()  # Duration in seconds.
    products = models.ManyToManyField(Product, related_name="lessons")

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_views")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="user_views")
    view_time = models.FloatField(default=0)
    last_view_date = models.DateField(null=True, blank=True)

    # The status “Viewed" is indicated if the user has viewed 80% of the video.
    viewed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.view_time >= 80:
            self.viewed = True
        else:
            self.viewed = False

    def __str__(self):
        return f"LessonView for {self.lesson} by {self.user}"
