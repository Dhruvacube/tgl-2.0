from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.safestring import mark_safe
import uuid
from django.conf import settings
from payments.models import *


# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=200, help_text=_('The name of the game'))
    short_description = models.TextField(help_text=_('About this short event, better keep it in between 100 characters'), validators=[MinLengthValidator(13),MaxLengthValidator(200)])
    long_description = models.TextField(help_text=_('Here explain everything'))
    image_url = models.URLField(help_text=_('Url of the game image'))
    platform = models.CharField(max_length=11,choices=(('a','ALL'),('m','Mobile'),('p','PC'),('ps','Play Station')), default='A')
    
    has_solo_entry = models.BooleanField(default=True)
    solo_entry = models.IntegerField(help_text='Enter the Solo entry price')
    
    has_squad_entry = models.BooleanField(default=True)
    squad_entry = models.IntegerField(help_text='Enter the Sqaud entry price')
    squad_entry_members = models.IntegerField(default=5)
    
    def __str__(self):
        return self.name

    def view_image(self):
        if self.image_url:
            return mark_safe(f'<img loading="lazy" src="{self.image_url}" width="50%" height="50%" />')
        else:
            return 'None'
    
    
    class Meta:
        verbose_name_plural = _('Games')

class GameGroup(models.Model):
    group_name = models.CharField(max_length=250)
    group_unique_id= models.UUIDField(default=uuid.uuid4)
    solo_or_squad = models.CharField(default='sq', choices=(('sq','SQUAD'),('so','SOLO')),max_length=15)
    game=models.ForeignKey(Games,on_delete=models.CASCADE)
    users=models.ManyToManyField(settings.AUTH_USER_MODEL)
    payment_id = models.ForeignKey(Payments ,on_delete=models.CASCADE, help_text=_('This is to be filled by computer'))
    
    def __str__(self):
        return str(self.group_name)
    