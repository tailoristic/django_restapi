from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def product_data(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = ProductSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
