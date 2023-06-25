# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *

print("1. Get the user information about learner `David`")
learner_david = Learner.objects.get(first_name="David")
print(learner_david.user_ptr) #<HINT> use the usr_ptr field created by Django for the Inheritance relationship#
print("2. Get learner `David` information from user")
user_david = User.objects.get(first_name="David")
print(user_david.learner) #<HINT> use the learner field created by Django#
print("3. Get all learners for `Introduction to Python` course")
course = Course.objects.get(name='Introduction to Python')
learners = course.learners.all() #<HINT> use the learners field in Course model# 
print(learners)
print("4. Check the occupation list for the courses taught by instructor `Yan`")
courses = Course.objects.filter(instructors__first_name = "Yan") #<HINT> query the first name of instructor#
occupation_list = set()
for course in courses:
    for learner in course.learners.all(): #<HINT>use the learners field in Course Model#  :
        occupation_list.add(learner.occupation)
print(occupation_list)
print("5. Check which courses developers are enrolled in Aug, 2020")  
enrollments = Enrollment.objects.filter(    date_enrolled__month=8,
                                            date_enrolled__year=2020,
                                            learner__occupation = 'developer') #<HINT>use the occupation field from learner #
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print(courses_for_developers)
