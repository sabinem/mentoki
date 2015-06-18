# Templates

Here are some base templates and scripts. Most templates are located within the apps in a
folder /apps/<appname>/templates/<appname> according to Django recommendation.

## Status: 


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