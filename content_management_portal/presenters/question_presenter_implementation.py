from content_management_portal.interactors.presenters. \
		question_presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.interactors.storages.dtos import QuestionDto
from content_management_portal.constants.exception_messages \
    import INVALID_QUESTION_ID

		
class PresenterImplementation(PresenterInterface):
	
	def raise_invalid_question_exception(self):
	        raise NotFound(*INVALID_QUESTION_ID)
	        
	def get_question_dto_response(self,questiondto: QuestionDto):
	        response_dict = {
	                          "question_id": questiondto.question_id,
	                          "short_title": questiondto.short_title,
	                          "problem_description": {
	                            "content_type": questiondto.content_type,
	                            "content": questiondto.content
	                          }
	                        }
	        return response_dict
