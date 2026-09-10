from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict


class AResponse:

    def __init__(self, message: str):
        self.__reason_code = status.HTTP_200_OK
        self.__message = message
        self.__data = None

    def set_data(self, data: Serializer | None = None):
        self.__data: Serializer | None = data

    def get_data(self) -> Serializer | None:
        return self.__data

    def set_message(self, message: str | None):
        self.__message: str | None = message

    def get_message(self) -> str | None:
        return self.__message

    def set_reason_code(self, status_code: int = status.HTTP_200_OK):
        self.__reason_code = status_code

    def get_reason_code(self) -> int:
        return self.__reason_code

    def serialize(self) -> Response:
        return Response(self.__generate_body__(), status=self.__reason_code)

    def __generate_body__(self):
        resp_data: ReturnDict | None = None

        if self.get_data() is not None:
            resp_data = self.get_data().data

        return {
            "message": self.get_message(),
            "reason_code": self.get_reason_code(),
            "data": resp_data,
        }

