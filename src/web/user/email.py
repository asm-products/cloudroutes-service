#####################################################################
# Runbook Web Application
# ------------------------------------------------------------------
# Send registraton confirmation email
#####################################################################

from web import app, mandrill


def send_email(to, subject, template):
    mandrill.send_email(
        from_email=app.config['MAIL_DEFAULT_SENDER'],
        subject=subject,
        to=[to],
        template_name=template
    )
