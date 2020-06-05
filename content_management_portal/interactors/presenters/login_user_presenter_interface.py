from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import AccessTokenDTO

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_password_exception(self, username: str, password: str):
        pass

    @abstractmethod
    def raise_invalid_user_name_exception(self):
        pass

    @abstractmethod
    def get_response_for_access_token(self,access_token: str):
        pass