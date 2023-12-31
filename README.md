# DjangoTestProject
Executed architecture based on SQLite database using Django. Implemented APIs based on a ready-made architecture.
## 1. Building an architecture
### 1.1 Product
Create a product entity. The product must have an owner. You need to add an entity to save access to the product for the user.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/3bf2baba-eff2-4fe1-82bd-17e53966f35f)

### 1.2 Lesson
Create a lesson entity. The lesson can be in several products at the same time. The lesson should contain basic information: the title, the link to the video, the duration of viewing (in seconds).
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/ca1ba49f-c39a-46f8-91dd-51d7ec0c243b)


### 1.3 Viewed
The lesson can be viewed by many users. It is necessary to record the viewing time for each and record the status “Viewed”/”Not viewed.” The status “Viewed" is indicated if the user has viewed 80% of the video.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/3a8a5728-10c4-4f8c-8005-67f96f1f65b6)

## 2. Writing API

### 2.1 All lessons
Implement an API for displaying a list of all lessons for all products that the user has access to, with information about the status and viewing time.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/8f8ff246-b7fa-41d1-98f0-fb3956b80674)


### 2.2 Lessons for special product
Implement an API with displaying a list of lessons for a specific product to which the user has access, with displaying information about the status and viewing time, as well as the date of the last viewing of the video.
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/47c612d9-5db2-4bdb-b082-976b15f6da1c)


### 2.3 Statistics
Implement an API for displaying product statistics. It is necessary to display a list of all products on the platform, attach information to each product:
The number of lessons viewed from all students.
How much time did all the students spend watching the videos in total?
The number of students engaged in the product.
The percentage of product purchase (calculated based on the number of accesses to the product divided by the total number of users on the platform).
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/8e37d919-0485-4d26-9180-c804a5fab132)


## Registration
### Adding user
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/7b05f320-8679-4f74-ac18-c6bcde87f050)
### Getting token
![image](https://github.com/GarlicRoll/DjangoTestProject/assets/75137969/e6391db1-386d-45e2-af0c-348f653fa266)

(The data is filled in using the change_existing_data.py script, assumes three users)

