from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Scan_Vul, Certification, Comment, Profile, reatingProfile

from .serializers import Scan_VulSerializer, CertificationSerializer, ProfileSerializer, CommentSerializer, ReatingProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


# ADD, View, Update, and Delete new Vulnerabilities by the Scanner.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_Scan_Vul(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.add_scan_vul'):
        return Response({"msg": "Sorry, Not Allowed to add vulnerabilities ..."}, status=status.HTTP_401_UNAUTHORIZED)

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
@permission_classes([IsAuthenticated])
def update_Scan_Vul(request: Request, vulner_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.change_scan_vul'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)
    scan_Vul = Scan_Vul.objects.get(id=vulner_id)

    updated_vul = Scan_VulSerializer(instance=scan_Vul, data=request.data)
    if updated_vul.is_valid():
        updated_vul.save()
        responseData = {
            "msg": "updated vulnerability successefully"
        }

        return Response(responseData)
    else:
        print(updated_vul.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_vulnerability(request: Request, vulner_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.delete_scan_vul'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    scan_Vul = Scan_Vul.objects.get(id=vulner_id)
    scan_Vul.delete()
    return Response({"msg": "DELETE Vulnerability Successfully"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def search_vulnerabilityOS(request: Request, vul_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    scan_Vul = Scan_Vul.objects.filter(type_OS=vul_id)

    dataResponse = {
        "msg": "the vulnerability :",
        "scan_Vulnerability": Scan_VulSerializer(instance=scan_Vul, many=True).data
    }

    return Response(dataResponse)


# ADD, View, Update, and Delete Certifications by the Specialist CyberSecurity

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_Certification(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.add_certification'):
        return Response({"msg": "Sorry, Not Allowed to add Certification ..."}, status=status.HTTP_401_UNAUTHORIZED)

    NewCertification = CertificationSerializer(data=request.data)
    if NewCertification.is_valid():
        NewCertification.save()
        dataResponse = {
            "msg": "Thank you for record this NewCertification...",
            "Certification ": NewCertification.data
        }
        return Response(dataResponse)
    else:
        print(NewCertification.errors)
        dataResponse = {"msg": "Sorry, couldn't add new Certification..."}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_Certification(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    certification = Certification.objects.all()
    dataResponse = {
        "msg": "list of  certifications in 2022",
        "Vulnerabilities": CertificationSerializer(instance=certification, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_Certification(request: Request, cer_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.change_certification'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)
    certification = Certification.objects.get(id=cer_id)

    updated_cer = CertificationSerializer(instance=certification, data=request.data)
    if updated_cer.is_valid():
        updated_cer.save()
        responseData = {
            "msg": "updated Certification successefully"
        }

        return Response(responseData)
    else:
        print(updated_cer.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_Certification(request: Request, cer_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.delete_certification'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    cer = Certification.objects.get(id=cer_id)
    cer.delete()
    return Response({"msg": "DELETE Certification Successfully"})


# ADD, View, Update, and Delete Profile by the Specialist CyberSecurity

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_Profile(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.add_profile'):
        return Response({"msg": "Sorry, Not Allowed to add Profile Specialist CyberSecurity ..."},
                        status=status.HTTP_401_UNAUTHORIZED)

    NewProfile = ProfileSerializer(data=request.data)
    if NewProfile.is_valid():
        NewProfile.save()
        dataResponse = {
            "msg": "Thank you for record this Profile...",
            "Certification ": NewProfile.data
        }
        return Response(dataResponse)
    else:
        print(NewProfile.errors)
        dataResponse = {"msg": "Sorry, couldn't add new Profile..."}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_profile(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    profile = Profile.objects.all()
    dataResponse = {
        "msg": "list of  Specialists CyberSecurity profiles in 2022",
        "Vulnerabilities": ProfileSerializer(instance=profile, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request: Request, profile_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.change_profile'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)
    profile = Profile.objects.get(id=profile_id)

    updated_profile = ProfileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg": "updated profile successefully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request: Request, profile_id):
    if not request.user.is_authenticated or not request.user.has_perm('SecurityApp.delete_profile'):
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg": "DELETE profile Successfully"})

# CREATE,AND VIEW  COMMENT

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_comment(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Sorry, Not Allowed to add Profile Specialist CyberSecurity ..."},
                        status=status.HTTP_401_UNAUTHORIZED)

    NewComment = CommentSerializer(data=request.data)
    if NewComment.is_valid():
        NewComment.save()
        dataResponse = {
            "msg": "Thank you for record this Comment...",
            "Certification ": NewComment.data
        }
        return Response(dataResponse)
    else:
        print(NewComment.errors)
        dataResponse = {"msg": "Sorry, couldn't add new comments..."}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_comments(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    comment = Comment.objects.all()
    dataResponse = {
        "msg": "list of  Specialists CyberSecurity profiles in 2022",
        "Vulnerabilities": CommentSerializer(instance=comment, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def search_comment(request: Request, certification_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    comment = Comment.objects.filter(certification=certification_id)

    dataResponse = {
        "msg": "the comments :",
        "Comments": CommentSerializer(instance=comment, many=True).data
    }

    return Response(dataResponse)


# Rating for Specialist CyberSecurity Profile

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_ratting(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Sorry, Not Allowed to add Profile Specialist CyberSecurity ..."},status=status.HTTP_401_UNAUTHORIZED)

    rate = ReatingProfileSerializer(data=request.data)
    if rate.is_valid():
        rate.save()
        dataResponse = {
            "msg": "Thank you for record this Rating...",
            "Certification ": rate.data
        }
        return Response(dataResponse)
    else:
        print(rate.errors)
        dataResponse = {"msg": "Sorry, couldn't add new rate..."}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_reatingProfile(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    reate = reatingProfile.objects.all()
    dataResponse = {
        "msg": "list of Rating Specialists CyberSecurity ",
        "Vulnerabilities": ReatingProfileSerializer(instance=reate, many=True).data
    }
    return Response(dataResponse)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def search_ByRating(request: Request, rating_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed please LOGIN..."}, status=status.HTTP_401_UNAUTHORIZED)

    rate = reatingProfile.objects.filter(rate=rating_id)

    dataResponse = {
        "msg": "the vulnerability :",
        "scan_Vulnerability": ReatingProfileSerializer(instance=rate, many=True).data
    }

    return Response(dataResponse)

