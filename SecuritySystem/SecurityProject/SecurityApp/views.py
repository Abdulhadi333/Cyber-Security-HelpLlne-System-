from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Scan_Vul, Certification, Comment, Profile

from .serializers import Scan_VulSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_Scan_Vul(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    NewScan_Vul = Scan_VulSerializer(data=request.data)
    if NewScan_Vul.is_valid():
        NewScan_Vul.save()
        dataResponse = {
            "msg": "Thank you for record this vulnerability...",
            "ScannerVulnerability ": NewScan_Vul.data
        }
        return Response(dataResponse)
    else:
        print(NewScan_Vul.errors)
        dataResponse = {"msg": "Sorry, couldn't add new vulnerabillity..."}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_Scan_Vul(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    scan_Vul = Scan_Vul.objects.all()
    dataResponse = {
        "msg": "New vulnerabilities in the world",
        "Vulnerabilities": Scan_VulSerializer(instance=scan_Vul, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_Scan_Vul(request: Request, vulner_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)
    note = Scan_Vul.objects.get(id=vulner_id)

    updated_note = Scan_VulSerializer(instance=note, data=request.data)
    if updated_note.is_valid():
        updated_note.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_note.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)
