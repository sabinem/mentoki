from datetime import datetime
import pytz
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils import timezone



def get_current_time():
    tz = pytz.timezone('Europe/Zurich')
    return datetime.now(tz)

def validate_date_future(value):
    if value < get_current_time():
        #msg = u'Datum muss in der Zukunft liegen'
        #raise ValidationError(msg)
        pass


