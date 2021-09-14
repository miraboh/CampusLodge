from django.db import models


class CampusSchool(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % (self.name)
