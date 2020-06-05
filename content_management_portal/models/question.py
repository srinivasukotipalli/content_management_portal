from django.db import models
from content_management_portal.models.user import User
from content_management_portal.constants.enums import TextType

class Question(models.Model):

    Text_Choice = [(text_type.value,text_type.value) for text_type in TextType]


    short_title = models.CharField(max_length=100)
    content = models.TextField()
    content_type = models.CharField(max_length=20, choices=Text_Choice)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='questions', \
                    on_delete=models.CASCADE)
