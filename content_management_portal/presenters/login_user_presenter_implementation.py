from content_management_portal.interactors.presenters. \
    login_user_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import INVALID_USERNAME, INVALID_PASSWORD
from django_swagger_utils.drf_server.exceptions import NotFound


class PresenterImplementation(PresenterInterface):

    def raise_invalid_user_name_exception(self):
        raise NotFound(*INVALID_USERNAME)

    def raise_invalid_password_exception(self):
        raise NotFound(*INVALID_PASSWORD)


    def get_response_for_access_token(self,access_token: str):
                authorization_details = {
                    "access_token":access_token
                    # "refresh_token":refresh_token
                }
                return authorization_details

