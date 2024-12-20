from django.core.mail import send_mail


def send_email(request,**kwargs):
  subject = kwargs.get('subject','')
  body = kwargs.get('body','')
  title = kwargs.get('title','')
  to_email = kwargs.get('to_email','')
  title = "Photo Studio"
  
  mail_sent = send_mail(
    subject = subject,
    message = body,
    from_email = f'{title} <pankajtrsrewa@gmail.com>',
    recipient_list = [to_email],
    fail_silently = False,
  )
  if mail_sent:
    return {"success":True}


  # send_mail( subject='Subject', message='This is a test email from Django.', from_email='pkrm.in <pankajtrsrewa@gmail.com>', recipient_list=['pankaj.django@gmail.com'], fail_silently=False, )