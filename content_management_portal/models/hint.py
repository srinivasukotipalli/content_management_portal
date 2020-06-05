from django.db import models
from content_management_portal.models.question import Question

from content_management_portal.constants.enums import TextType

class Hint(models.Model):

    Text_Choice = [(text_type.value,text_type.value) for text_type in TextType]

    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100,choices=Text_Choice)
    content = models.TextField()
    order_id = models.IntegerField(default=1)
    question = models.ForeignKey(Question, related_name='hints', \
                    on_delete=models.CASCADE)
