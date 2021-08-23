from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# MODEL OBJECT - Single Student Data


def student_details(request, pk):
    student = Student.objects.get(id=pk)  # Complex Data
    serializer = StudentSerializer(student)  # Converting to python object
    jsonData = JSONRenderer().render(serializer.data)  # Converted to JSON frmat
    # Sending Data to user
    return HttpResponse(jsonData, content_type='application/json')

# QUERY SET - All Student Data


def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    # jsonData = JSONRenderer().render(serializer.data)
    # return HttpResponse(jsonData, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            jsonData = JSONRenderer().render(serializer.data)
            return HttpResponse(jsonData, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        jsonData = JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData, content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data) # COMPLETE UPDATE
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data = python_data, partial=True) # PARTIAL UPDATE
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            student.delete()
            res = {'msg': 'Data Deleted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def student_api(request):
    # ! GET API
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            jsonData = JSONRenderer().render(serializer.data)
            return HttpResponse(jsonData, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        jsonData = JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData, content_type='application/json')
    
    # ! POST API
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data) # COMPLETE UPDATE
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
    # ! PUT API
    # ? FOR UPDATE USE `PUT` METHOD ONLY 
    # ? COMPLETE UPDATE StudentSerializer(student, data = python_data)
    # ? FOR PARTIAL UPDATE USE `partial = True`
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data = python_data, partial=True) # PARTIAL UPDATE
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
     # ! DELETE API
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            student.delete()
            res = {'msg': 'Data Deleted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    