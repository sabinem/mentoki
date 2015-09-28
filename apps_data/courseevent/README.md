# App Courseevent
Courseevents are about an event which is based of the teaching material of a course
## CourseEvent
The following Models belong to the course app:
### Announcement
Emails that are send to the Participants of the Course
### Forum 
A Forum with Subforum, Threads and Posts
### CourseEventParticipation
Participants of a course
### Menu
The classroom Menu

## Interface to other apps: 
    CourseEvent.public_ready_for_booking.all()
All courseevents that are ready for public booking

    CourseEvent.public_ready_for_preview.all()
All courseevents that are ready for public booking
 
    CourseEvent.objects.get_courseevent_or_404_from_slug(self, slug): 
get one courseevent from slug    
 

