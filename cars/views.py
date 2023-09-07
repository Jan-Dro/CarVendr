from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Advertisement
from django.contrib.auth.models import User
from .serializers import AdvertisementSerializer

# Create your views here.
class AllAdvertisements(APIView):
    
    def get(self,request):
        advertisements = Advertisement.objects.order_by("id")
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)

class SelectedAdvertisement(APIView):

    def get_advertisement(self, id):
        if type(id) == int:
            return [Advertisement.objects.get(id = id)]
        else:
            advertisements = Advertisement.objects.filter(seller_account__username=id)
            if advertisements.count() > 1:
                return advertisements
            else:
                return [advertisements.first()]

    def get(self, request, id):
        advertisements = self.get_advertisement(id)
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)


