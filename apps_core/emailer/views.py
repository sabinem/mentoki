

from email_extras.utils import send_mail_template

send_mail_template(subject, template, addr_from, addr_to,
    fail_silently=False, attachments=None, context=None,
    headers=None)
