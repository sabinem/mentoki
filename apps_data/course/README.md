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

* blocks
* lessons
* lessonsteps



### accessible by the public:
* home (app): all info pages accessible to the public, that do not relate to classes.
* contact (app) : all contact forms for unregistered users 
* courseevent (app): courseevents the public might book (so far booking itself is not yet activated)

### only accessed by logged in users:
* *desk*: (app): starting point for all registered users, from where they access classes or class preperations. 
* course (app): A course is where all the coursematerial is gathered. A course serves as base for several courseevents.
* classroom (app): each courseevent comes with a classroom
* forum(app): the forum belongs to the classroom or courseevent

### auxiliary apps
* core (app): some common functions
* upload (app): for the upload of images
* pdf (app): no longer in use, will be deleted as soon as I figure out how to do this in a safe way (it is part of some migrations)

#The two Central Apps and their models:
### Course App
The course is the central app for teachers. Teachers own courses. This is where all their material resides. 
Their material is further structured into *blocks*, *lessons* and *materials*. This is a hierarchical structure with 
blocks on top and materials at the bottom. So far lower levels such as a material can't exist without belonging
to a higher level and delete is cascading. 
####Models:
* Course (Course Base)
* CourseOwner (The team teaching the Course)
* CourseBlock (Lessons that belong together, and will be treated as one block in the classroom menu)
* CourseUnit (Lesson, belongs to a Block)
* CourseMaterialUnit (Material, belongs to a CourseUnit)
###Courseevent-App
The actuall classes are courseevents. 
Students are not registered for course, but for courseevents. Courseevents come in a variety of formats 
like selflearning, selflearning with  a coach or group learning. There can be several courseevents build upon a course, 
which actually is the norm since courseevents will be repeated with the same coursematerial for several times.
####Models:
* CourseEvent (core attributes of the courseevent, that are needed for processing)
* CourseEventPubicInformation (Attributes describing the courseevent, in 1-1 relation with the courseevent)
* CourseEventParticipation (users that are participating as students)
* CourseeventUnitPublish (Lessons that have been published in that courseevent)

#Status Doku:

#Status Tests:
