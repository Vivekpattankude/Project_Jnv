from rest_framework import generics
from .models import Batches
from .serializers import BatchesSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# from apps.Batches.serializers import BatchesSerializer


# Create your views here.
class BatchesList(generics.ListCreateAPIView):
    queryset = Batches.objects.all()
    serializer_class = BatchesSerializer

class BatchesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batches.objects.all()
    serializer_class = BatchesSerializer
    









    

# @csrf_exempt
# def batchesApi(request,id=0):
#     if request.method=='GET':
#         batches = Batches.objects.all()
#         batches_serializer = BatchesSerializer(batches, many=True)
#         return JsonResponse(batches_serializer.data, safe=False)

#     elif request.method=='POST':
#         batches_data=JSONParser().parse(request)
#         batches_serializer = batchesSerializer(data=employee_data)
#         if batches_serializer.is_valid():
#             batches_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         batches_data = JSONParser().parse(request)
#         batches=Batchess.objects.get(BatchesId=batches_data['BatchesId'])
#         batches_serializer=BatchesSerializer(batches,data=batches_data)
#         if batches_serializer.is_valid():
#             batches_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         batches=Batchess.objects.get(BatchesId=id)
#         batches.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)