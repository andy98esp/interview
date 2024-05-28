from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django import setup

from application.serializers import InterViewModelSerializer

setup()
from application.models import InterViewModel


class InterviewApi(APIView):

    @staticmethod
    def get(request):
        return Response({"response": "Hello World!"}, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serialized_data = InterViewModelSerializer(data=request.data)
        if serialized_data.is_valid():
            interview, _ = InterViewModel.objects.get_or_create(
                field1=serialized_data.data['field1']
            )
            if not _:
                return Response({"response": f"Interview instance with field1 = {interview.field1} already in our database"}, status=status.HTTP_200_OK)
            return Response({"response": f"Interview {interview.field1} created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        serialized_data =
        try:
            interview = InterViewModel.objects.get(field1=request.data['field1'])

    def delete(self, request, *args, **kwargs):
        """"""
