from django.db import models
from content_management_portal.models.question import Question

from content_management_portal.constants.enums import CodeLanguage


class CleanSolution(models.Model):

    CODE_CHOICES = [(language.value,language.value)for language in CodeLanguage]


    code = models.TextField()
    code_type = models.CharField(max_length=20, choices=CODE_CHOICES)
    filename = models.CharField(max_length=100)
    question = models.ForeignKey(Question, related_name='clean_solutions', \
                    on_delete=models.CASCADE)
