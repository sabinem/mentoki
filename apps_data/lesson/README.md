# App Course
Course is the central app of the platform. A course gathers all the teaching material and 
lessons for a topic and by a team of teachers. The material belongs to the teaching team.
The course is the foundation for courseevents that build upon it and select which pieces of the
course they will show at what time.

## Models 
The following Models belong to the course app:
###Course
Contains a description of the ideal course: what is about. This description will not be used for
the actual courseevents, but is rather a base construct where courseevents copy from 
and which they specialize. 
Example: A course could be about "Learning to achieve your goals. Then the course would gather all
the material that the teachers has about that topic. He can then make courseevents upon that:
* a guided group course with a start and end date
* a self paced self learning course, that presents the material in a structured manner
###Lesson 
The Lessons are all in this module. It is realised with mptt. Even though the lessons are all
in the same database-table and have the same structure, they are considered differently, depending on 
their level
* level 0 are *blocks*: the roots of a bunch lessons, that belong together
* level 1 are *lessons*: the unit that will be shown to the student in a coursevent: material for 1 week
* level 2 are *steps*: the lessons are broken down in steps
### CourseOwner
A course can have more then one owners
### Material
Material that has been uploaded and integrated in the course
A lesson can have 0-many materials attached to it.

## Interface to other apps: 
### Course 
#### Attributes
* teachers: user-objects of the teachers teaching the course, ordered by head-teacher and assistant-teacher
* teachersrecord: the string that will be shown regarding the teachers of the course on the coursedescription derived from the teachers
#### Manager

####Queries
    Course.objects.get_course_or_404_from_slug(slug=...)
get course object
    
####Attributes of Course
    teachers
List of teachers as user objects

    teachersrecord
Teachers first and last name in the right order: head teacher first, then assistant teacher

## Datamigration
So far I did all the datamigration with shell scripts, which are written down in the datemigrations folder

## Questions

## Future Projects

### Implement some app for versioning or audit trail:
* http://django-audit-log.readthedocs.org/en/latest/: keeps track of created/changed_by with user and session_id
* http://django-simple-history.readthedocs.org/en/latest/: provides versions

