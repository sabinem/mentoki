# App Course
Course is the central app. Here is all the data that teachers need to plan their lessons.

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

## Status: 
I am redesigning this app in the moment. There are some old models in the file oldcoursepart 
and some corresponding fields in the new models. They will be deleted as sonn as the data has been transfered. 


