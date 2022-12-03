from django.db import models

# Create your models here.

states = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Rider(models.Model):
    first = models.CharField(max_length=16)
    last = models.CharField(max_length=16)
    email = models.CharField(max_length=100, default= '')
    password = models.CharField(max_length=16, default='')
    sex = models.CharField(max_length=7)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first + ' ' + self.last


class Race(models.Model):
    name = models.CharField(default= "",max_length=24)
    city = models.CharField(max_length=16)
    state = models.CharField(max_length=16, choices=states)
    distance = models.CharField(choices=(('mini','mini'),('short','short'),('long','long'),('ultra', 'ultra')), max_length=16)
    date = models.DateField()
    time = models.TimeField()
    riders = models.ManyToManyField(Rider)
    
    def __str__(self):
        return self.name