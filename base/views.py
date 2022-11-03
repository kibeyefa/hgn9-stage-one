from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SlackDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'slackUsername': 'kibeyefa',
            'backend': True,
            'age': 21,
            'bio': "",
        }

        return Response(data=data)

    def post(self, *args, **wargs):
        pass
