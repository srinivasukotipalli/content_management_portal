from django.db import models
from content_management_portal.models.question import Question

from content_management_portal.constants.enums import CodeLanguage

class Case(models.Model):

    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    is_hidden = models.BooleanField()
    score = models.IntegerField()
    order_id = models.IntegerField(default=1)
    question = models.ForeignKey(Question, related_name='test_cases', \
                    on_delete=models.CASCADE)
