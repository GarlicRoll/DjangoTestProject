# DjangoTestProject
Executed architecture based on SQLite database using Django. Implemented APIs based on a ready-made architecture.
## 1. Building an architecture
### 1.1
Create a product entity. The product must have an owner. You need to add an entity to save access to the product for the user.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/3bf2baba-eff2-4fe1-82bd-17e53966f35f)

### 1.2
Create a lesson entity. The lesson can be in several products at the same time. The lesson should contain basic information: the title, the link to the video, the duration of viewing (in seconds).
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/7cf8e5af-2555-42b6-af92-0f8d770636d3)

### 1.3
The lesson can be viewed by many users. It is necessary to record the viewing time for each and record the status “Viewed”/”Not viewed.” The status “Viewed" is indicated if the user has viewed 80% of the video.

## 2. Writing API

### 2.1
Implement an API for displaying a list of all lessons for all products that the user has access to, with information about the status and viewing time.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/ac93995f-1c80-4c61-85b6-542330a02c12)

### 2.2
Implement an API with displaying a list of lessons for a specific product to which the user has access, with displaying information about the status and viewing time, as well as the date of the last viewing of the video.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/ba2b0de6-df4f-41e5-9688-0846875dfddf)

### 2.3
Implement an API for displaying product statistics. It is necessary to display a list of all products on the platform, attach information to each product:
The number of lessons viewed from all students.
How much time did all the students spend watching the videos in total?
The number of students engaged in the product.
The percentage of product purchase (calculated based on the number of accesses to the product divided by the total number of users on the platform).
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/c869f8ff-102d-4c6f-baef-a168047c6373)

## Registration
### Adding user
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/7b05f320-8679-4f74-ac18-c6bcde87f050)
### Getting token
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/e6391db1-386d-45e2-af0c-348f653fa266)

(The data is filled in using the change_existing_data.py script, assumes three users)

