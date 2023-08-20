from django.db import models

class TODO(models.Model):
    item=models.CharField(max_length=200)
    isComplete=models.BooleanField(default=False)

    class Meta:
        indexes=[models.Index(fields=['item', 'isComplete'])]
