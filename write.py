# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


#Code starts from here:
def write_instructors():
    # Add instructors
    # Create a user
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16), full_time=True, total_learners=30050)
    instructor_yan.save()
    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved... ")

def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()
    print("Course objects all saved... ")


def write_lessons():
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.save()
    print("Lesson objects all saved... ")

def write_learners():
    # Add Learners
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()

    #first_name, last_name, dob, occupation, social_link
    learner_fer = Learner(first_name='Fernando', last_name='Alonso', dob=date(1982, 5, 11)
                          , occupation='student', social_link='https://www.linkedin.com/fernando/')
    learner_fer.save()

    learner_peter = Learner(first_name='Peter', last_name='Greaffing', dob=date(1975, 1, 25)
                            , occupation='student', social_link= 'https://www.linkedin.com/peter/')
    learner_peter.save()

    learner_samuel = Learner(first_name='Samuel', last_name='Eto', dob=date(1979, 11, 30)
                             , occupation='developer', social_link='https://www.linkedin.com/samuel/')
    learner_samuel.save()
    print("Learner objects all saved... ")

def populate_course_instructor_relationships():
    #Adding instructors to each course
    courses = Course.objects.all()
    instructors = Instructor.objects.all()
    courses[0].instructors.add(instructors[0], instructors[1])
    courses[1].instructors.add(instructors[2], instructors[3])
    print("All fine!")

def populate_course_enrollment_relationships():
    #Gettings all courses Total = 2
    courses = Course.objects.all()
    learners = Learner.objects.all() #Total learners = 8

    enrollment_learner_1 = Enrollment(date_enrolled = date(2023, 6, 1), mode = 'honor', course = courses[0], learner = learners[0])
    enrollment_learner_1.save()
    print("Learner " + learners[0].last_name + ", enrolled successfully")

    enrollment_learner_2 = Enrollment(date_enrolled = date(2023, 6, 1), course = courses[1], learner = learners[1])
    enrollment_learner_2.save()
    print("Learner " + learners[1].last_name + ", enrolled successfully")

    enrollment_learner_3 = Enrollment(date_enrolled = date(2023, 6, 3), course = courses[0], learner = learners[2])
    enrollment_learner_3.save()
    print("Learner " + learners[2].last_name + ", enrolled successfully")

    enrollment_learner_4 = Enrollment(date_enrolled = date(2023, 6, 5), mode = 'honor', course = courses[1], learner = learners[3])
    enrollment_learner_4.save()
    print("Learner " + learners[3].last_name + ", enrolled successfully")

    enrollment_learner_5 = Enrollment(date_enrolled = date(2023, 6, 4), course = courses[1], learner = learners[4])
    enrollment_learner_5.save()
    print("Learner " + learners[4].last_name + ", enrolled successfully")

    enrollment_learner_6 = Enrollment(date_enrolled = date(2023, 6, 4), course = courses[1], learner = learners[5])
    enrollment_learner_6.save()
    print("Learner " + learners[5].last_name + ", enrolled successfully")

    enrollment_learner_7 = Enrollment(date_enrolled = date(2023, 6, 2), mode = 'honor', course = courses[0], learner = learners[6])
    enrollment_learner_7.save()
    print("Learner " + learners[6].last_name + ", enrolled successfully")

    enrollment_learner_8 = Enrollment(date_enrolled = date(2023, 6, 5), course = courses[1], learner = learners[7])
    enrollment_learner_8.save()
    print("Learner " + learners[7].last_name + ", enrolled successfully")

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()

# Clean any existing data first
#clean_data()
#write_courses()
#write_instructors()
#write_lessons()
#write_learners()
#populate_course_instructor_relationships()
populate_course_enrollment_relationships()