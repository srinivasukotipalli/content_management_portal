from django.db import models
from content_management_portal.models.question import Question

from content_management_portal.constants.enums import TextType

class SolutionApproach(models.Model):

    Text_Choice = [(text_type.value,text_type.value) for text_type in TextType]

    title = models.CharField(max_length=100)
    description_content_type = models.CharField(max_length=100,choices=Text_Choice)
    description_content = models.TextField()
    complexity_analysis_content_type = models.CharField(max_length=100,choices=Text_Choice)
    complexity_analysis_content = models.TextField()
    question = models.OneToOneField(Question, related_name='solution_approach', \
                                                on_delete=models.CASCADE)
