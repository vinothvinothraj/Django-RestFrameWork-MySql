from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CrudApp.serializers import CrudSerializer
from CrudApp.models import CrudExample

@csrf_exempt
def CrudExampleApi(request, id=0):
    if request.method == 'GET':
        crudexample = CrudExample.objects.all()
        crudexample_serializer = CrudSerializer(crudexample, many=True)
        return render(request, 'index.html', {'crud_examples': crudexample_serializer.data})

    elif request.method == 'POST':
        crudexample_data = JSONParser().parse(request)
        crudexample_serializer = CrudSerializer(data=crudexample_data)
        if crudexample_serializer.is_valid():
            crudexample_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        crudexample_data = JSONParser().parse(request)
        crudexample = CrudExample.objects.get(id=id)
        crudexample_serializer = CrudSerializer(crudexample, data=crudexample_data)
        if crudexample_serializer.is_valid():
            crudexample_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        crudexample = CrudExample.objects.get(id=id)
        crudexample.delete()
        return JsonResponse("Deleted Successfully", safe=False)
