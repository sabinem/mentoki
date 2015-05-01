![alt text](http://mentoki.com/static/img/mentoki_logo_untertitel.jpg "Logo Title Text 1")

# Mentoki Project
Mentoki is a platform for teaching and learning. The platform provides infrastructure to teachers or mentors
for holding up online classes. There will be a payment system integrated in the near future. So far it is not.
What is also still missing are extended user profiles.

##Structure
The platform splits up into a public part and a private part, that is only accessible by registered users, mostly
teachers and their students.
There are the following basic components that correspond to apps:

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

##The two Central Apps and their models:
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

