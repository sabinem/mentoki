![alt text](http://mentoki.com/static/img/mentoki_logo_untertitel.jpg "Logo Title Text 1")

# Mentoki Project
Mentoki is a platform for teaching and learning. The platform provides 
infrastructure to teachers/mentors for holding up online classes. 
For payments of the courses braintree is used as payment provider
#Structure
The platform splits up into a public part and a private part.
The private part is only accessible by registered users, mostly
teachers and their students.
Also generally data-handling and data-viewing are kept in seperate apps.

##Public apps
###apps-public

#App-Structure
* apps_data: handling data, models and the like
* apps_internal: handling views for registered users: classroom, teaching, etc.
* apps_public: handling views for unregisterd users
* apps_core: handling emails, uplaods, etc.
#Architecture(Apps)
###apps_data: 
handles the data
###apps_internal:
handles all views for registered teachers and learners and has two apps: one 
for the classroom activity and one for the teachers managing and setting up 
the classrooms.
###apps_public
manages the public face of the website
###apps_core
handles emails and central utilities
##Architecture(Elements)
There is a second structure that runs vertical to the first, since most
elements are found in different apps.
###Apps:
* apps_data: have their data
* apps_internal.classroom: handles their view in the classroom
* apps_internal.coursebackend: handles their setup by the teachers.
###Elements
* Announcements: communication from teachers to the class (few to many)
* Forum: communication within the class (many to many)
* Lessons: the units of lecture
* Material: is just the pdfs that are parts of lessons
* Studentswork: papers that students write in class
##Architecture(Course/Event)
There is a third structure concerning the differents between time independent
elements and elements that belong to a certain event such as an actual class,
that takes place. 
All Elements have representation in the Event, some have also representation
in the course, that serves as a time independent template. 
###Elements Representations
* Announcements: only in Event
* Forum: only in Event
* Lessons are found in both: Course and Event and may point to one another
* Materials are only stored for the Course
* Studentswork: only in Event
#Status of Tests and Doku
I will drive the status of tests and Doku forward by elements,
since this seems to make the most sense to me.
##Announcements:
###Apps
* data: apps_data.courseevent.models.announcement
* coursebackend: apps_internal.coursebackend.views.announcement
* classroom: apps_internal.classroom.views.announcement
###Status:
* logging: implemented
* doku: ready
* tests: missing
##Course:
###Apps
* data: apps_data.course.models.course
* coursebackend: apps_internal.coursebackend.views.course               
* coursebackend: apps_internal.coursebackend.views.courseowner     
###Status:
* logging: implemented
* doku: ready
* tests: missing
##CourseEvent:
##Lesson:
##ClassLesson:
##Material
##ClassroomMenu:
##Forum:
##StudentsWork:
##Accounts:
##Customers:
##Homepage:
##Public Courses:
