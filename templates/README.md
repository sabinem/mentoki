# Templates

Here are only the base templates

## account:
these templates overwrite the according django-allauth templates 

##base: these are the base templates 

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