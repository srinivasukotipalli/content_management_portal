from content_management_portal.interactors.storages.dtos \
    import QuestionDetailsDto
from content_management_portal.models import Question
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.storages.dtos import QuestionDetailsDto


class HomeStorageImplementation(StorageInterface):

    def get_question_details(self, offset: int, limit: int):

        question_query_set = \
                Question.objects.select_related('solution_approach') \
                                .prefetch_related(
                                       'rough_solutions',
                                       'test_cases',
                                       'prefilled_codes',
                                       'clean_solutions',
                                       'hints'
                                       ).all()

        total_coding_questions = len(question_query_set)

        total_questions_dtos_list = \
            [
                QuestionDetailsDto(
                    question_id = question.id,
                    short_title = question.short_title,
                    roughsolution = question.rough_solutions.all().exists(),
                    testcase = question.test_cases.all().exists(),
                    prefilledcode = question.prefilled_codes.all().exists(),
                    solutionapproach = self._check_solutionapproach_obj(question),
                    cleansolution = question.clean_solutions.all().exists(),
                    hint = question.hints.all().exists()
                    ) \
                    for question in question_query_set[offset:offset+limit]
            ]

        return total_questions_dtos_list,total_coding_questions

    @staticmethod
    def _check_solutionapproach_obj(question):
        try:
            return bool(question.solution_approach)
        except:
            return False
