from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request, room_name):
    return render(request, 'base/room.html',{"room_name": room_name})


def getToken(request):
    appId = "2c44d8ca8d8a46fabf18977bdd6f7db2"
    appCertificate = "39d33291793e496a9c5e8b19c6c05270"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


# new

def home(request):
    return render(request, 'base/home.html')
def base(request):
    return render(request, 'base/base.html')
def admin_portal(request):
    return render(request, 'base/admin_portal.html')
def Contact(request):
    return render(request, 'base/Contact.html')
def dashboard(request):
    return render(request, 'base/dashboard.html')
def login(request):
    return render(request, 'base/login.html')
def patient_view(request):
    return render(request, 'base/patient_view.html')
def register(request):
    return render(request, 'base/register.html')
def reports(request):
    return render(request, 'base/reports.html')
def beds(request):
    return render(request, 'base/beds.html')
def prescriptions(request):
    return render(request, 'base/prescriptions.html')
def vitals(request):
    return render(request, 'base/vitals.html')
