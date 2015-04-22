from __future__ import unicode_literals
import logging
import datetime

from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
from django.utils.translation import ugettext, ungettext_lazy
import math


logger = logging.getLogger(__name__)



def timesince(d, now=None, reversed=False):
    """
    Takes two datetime objects and returns the time between d and now
    as a nicely formatted string, e.g. "10 minutes".  If d occurs after now,
    then "0 minutes" is returned.

    Units used are years, months, weeks, days, hours, and minutes.
    Seconds and microseconds are ignored.  Up to two adjacent units will be
    displayed.  For example, "2 weeks, 3 days" and "1 year, 3 months" are
    possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.

    Adapted from
    http://web.archive.org/web/20060617175230/http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """
    chunks = (
        (60 * 60 * 24 * 730, ungettext_lazy('%d Jahren', '%d Jahren')),
        (60 * 60 * 24 * 365, ungettext_lazy('%d Jahr', '%d Jahr')),
        (60 * 60 * 24 * 60, ungettext_lazy('%d Monaten', '%d Monaten')),
        (60 * 60 * 24 * 30, ungettext_lazy('%d Monat', '%d Monat')),
        (60 * 60 * 24 * 14, ungettext_lazy('%d Wochen', '%d Wochen')),
        (60 * 60 * 24 * 7, ungettext_lazy('%d Woche', '%d Woche')),
        (60 * 60 * 48, ungettext_lazy('%d Tagen', '%d Tagen')),
        (60 * 60 * 24, ungettext_lazy('%d Tag', '%d Tag')),
        (60 * 120, ungettext_lazy('%d Stunden', '%d Stunden')),
        (60 * 60, ungettext_lazy('%d Stunde', '%d Stunde')),
        (120, ungettext_lazy('%d Minuten', '%d Minuten')),
        (60, ungettext_lazy('%d Minute', '%d Minute'))
    )
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)

    delta = (d - now) if reversed else (now - d)
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return avoid_wrapping(ugettext('0 minutes'))
    for i, (seconds, name) in enumerate(chunks):
        count = since // seconds
        if count != 0:
            break
    result = avoid_wrapping(name % count)
    # if i + 1 < len(chunks):
        # Now get the second item
    #    seconds2, name2 = chunks[i + 1]
    #   count2 = (since - (seconds * count)) // seconds2
    #   if count2 != 0:
    #       result += ugettext(', ') + avoid_wrapping(name2 % count2)
    return result





NUMBER_WORDS = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

def int_to_english(n):

    english_parts = []
    ones = n % 10
    tens = n % 100
    hundreds = math.floor(n / 100) % 10
    thousands = math.floor(n / 1000)

    if thousands:
        english_parts.append(int_to_english(thousands))
        english_parts.append('thousand')
        if not hundreds and tens:
            english_parts.append('and')
    if hundreds:
        english_parts.append(NUMBER_WORDS[hundreds])
        english_parts.append('hundred')
        if tens:
            english_parts.append('and')
    if tens:
        if tens < 20 or ones == 0:
            english_parts.append(NUMBER_WORDS[tens])
        else:
            english_parts.append(NUMBER_WORDS[tens - ones])
            english_parts.append(NUMBER_WORDS[ones])
    result = ' '.join(english_parts)
    return result.capitalize()


def depth(l):
    # calculates the depth of a list
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def date_ddmmyy(datetime):

    tag = datetime.day
    monat = datetime.month
    jahr = datetime.year
    stunde = datetime.hour
    minute = datetime.minute
    return "%02i.%02i.%04i %02i:%02i" % (tag,monat,jahr,stunde,minute)
