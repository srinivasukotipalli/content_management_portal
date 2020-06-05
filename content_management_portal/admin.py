from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import User 
from .models.question import Question
from .models.roughsolution import RoughSolution
from .models.cleansolution import CleanSolution
from .models.prefilledcode import PrefilledCode
from .models.testcase import Case
from .models.hint import Hint
from .models import SolutionApproach


admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(RoughSolution)
admin.site.register(Case)
admin.site.register(PrefilledCode)
admin.site.register(CleanSolution)
admin.site.register(Hint)
admin.site.register(SolutionApproach)
