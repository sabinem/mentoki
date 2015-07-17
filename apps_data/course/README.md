# App Course
Course is the central app. It is about the teaching material for a topic.

## Models 
The following Models belong to the course app:
###Course
Contains a description of the topic, the target-group, etc.
###Lesson 
The Lessons are all in this module. It is realised with mptt. Even though the lessons are all
in the same database-table and have the same structure, they are considered differently, depending on 
their level
* level 0 are *blocks*: the roots of a bunch lessons, that belong together
* level 1 are *lessons*
* level 2 are *steps* within a lesson
### CourseOwner
Teachers of a course
### Material
Material that has been uploaded and integrated in the course
A lesson can have 0-many materials attached

## Interface to other apps: 
###Course 
####Queries
    Course.objects.get_course_or_404_from_slug(slug=...)
get course object

    CourseOwner.objects.teacherinfo(course=...)
gets coursowners for a course    
    
####Attributes of Course
    teachers
List of teachers as user objects

    teachersrecord
Teachers first and last name in the right order: head teacher first, then assistant teacher


