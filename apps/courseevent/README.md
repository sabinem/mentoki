# App Courseevent

Courseevents are the units in this platform that can be booked. This apps handles everything around 
courseevents including the participation in them.

## Models 
+ CourseEvent
+ CourseeventUnitPublish
+ CourseEventParticipation

##Views and Templates
There are always public and internal views. Courseevents can be prebooked internaly by peers in
order to test them out, before they go life.

## Status: 
This app is being worked on.

##Questions:
### Are all of these attributes necessary?
+ excerpt = models.TextField(blank=True)
+ text = models.TextField(blank=True)
+ format = models.TextField(blank=True)
+ workload = models.TextField(blank=True)
+ project = models.TextField(default="x",blank=True)

### Event types:
+ (TYPE_TIMED_COURSE, 'Gruppenkurs'),
+ (TYPE_ONGOING, 'internes Diskussionsforum / ohne Termin / nicht gelistet '),
+ (TYPE_SELFLEARN_ATTENDED, 'unbegleitetes Selbstlernen / ohne Termin'),
+ (TYPE_SELFLEARN_UNATTENDED, 'begleitetes Selbstlernen / ohne Termin'),