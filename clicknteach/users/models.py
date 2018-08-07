
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    newsletter_reader = models.NullBooleanField( default=True,help_text="Select yes if you want to receive our newsletters.")


#    def clean(self):
#        from django.core.exceptions import ValidationError
#        if not self.subscriber:
#            raise ValidationError('CUSTOM ERROR HERE')
