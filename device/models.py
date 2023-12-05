from django.db import models

# Create your models here.

class StateTemplate(models.Model):
    name = models.TextField()

class StateTemplateFieldType(models.TextChoices):
    BYTE = 'BYTE', 'BYTE'

class StateTemplateField(models.Model):
    template = models.ForeignKey(StateTemplate, related_name='fields', on_delete=models.CASCADE)
    name = models.TextField()
    type = models.TextField(choices=StateTemplateFieldType.choices)
    ordinal = models.IntegerField()
    
    class Meta:
        unique_together = [['template', 'ordinal']]
        ordering = ['template', 'ordinal']

class Device(models.Model):
    address = models.CharField(max_length=5)
    state_template = models.ForeignKey(StateTemplate, on_delete=models.PROTECT)
