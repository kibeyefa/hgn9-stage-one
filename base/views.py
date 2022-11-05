from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SlackDetailsView(APIView):
    data = {
        "slackUsername": "kibeyefa",
    }

    def get(self, request, *args, **kwargs):
        self.data["backend"] = True,
        self.data["age"] = 21,
        self.data["bio"] = "I am Koboju Kibeyefa, a backend developer and student of The Federal University of Technology Akure.",
        return Response(data=self.data)

    def post(self, *args, **wargs):
        post_data = self.request.data
        operation = post_data.get('operation_type')
        x: int = post_data.get('x')
        y: int = post_data.get('y')

        result: int = 0

        if operation == 'addition':
            result = x + y
        elif operation == 'subtraction':
            result = x - y
        elif operation == 'multiplication':
            result = int(x * y)

        self.data['result'] = result
        self.data['operation_type'] = operation
        return Response(self.data)
