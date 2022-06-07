from cgitb import html
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serilizer import *
from .models import *

@api_view(['GET'])
def Getinfo(request):
    a = Info.objects.last()
    ser = InfoSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
def Getslider(request):
    b = Slider.objects.all().order_by('-id')[0:5]
    ser = SliderSerializer(b, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getprojects(request):
    c = Projects.objects.all()
    ser = ProjectsSerializer(c, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Gettechnopark(request):
    a = Technopark.objects.all()
    ser = TechnoparkSerilaizer(a, many=True)
    return Response(ser.data)
@api_view(['GET'])
def Getsection(request, pk):
    b = Section.objects.get(id=pk)
    ser = SectionSerializer(b)
    return Response(ser.data)

@api_view(['GET'])
def Getpostal(request):
    c = Postalservices.objects.all()
    ser = PostalSerializer(c, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Getboglanish(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    a = Boglanish.objects.create(fullname=fullname, phone=phone, text=text)
    ser = BoglanishSerializer(a)
    return Response(ser.data)
    
@api_view(['GET'])
def Getmobileoperators(request):
    e = Mobileoperators.objects.all()
    ser = MobileoperatorsSerializer(e, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getinternetproviders(request):
    f = Internetproviders.objects.all()
    ser = InternetprovidersSerializer(f, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getouraudience(request):
    g = OurAudience.objects.all()
    ser = OurAudienceSerializer(g, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getpercentage(request):
    h = Percentage.objects.all()
    ser = PercentageSerializer(h, many=True)
    return Response(ser.data)
@api_view(['GET'])
def Getresidents(request):
    i = Residents.objects.all()
    ser = ResidentsSerializer(i, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getteam(request):
    j = Team.objects.all()
    ser = TeamSerializer(j, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcoimages(request):
    k = Coimages.objects.all()
    ser = CoimagesSerializer(k, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcoworking(request):
    l = Coworking.objects.all()
    ser = CoworkingSerializer(l, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getinfrastructure(request):
    m = InfrastructureSlider.objects.all()
    ser = InfrastructureSliderSerializer(m, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getstudydirections(request):
    n = StudyDirections.objects.all()
    ser = StudydirectionsSerializer(n, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getitacademy(request):
    o = ItAcademy.objects.all()
    ser = ItAcademySerializer(o, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getstartupdirections(request):
    q = StartupDirections.objects.all()
    ser = StartupDirectionsSerializer(q, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getincubationcenters(request):
    r = IncubationCenters.objects.all()
    ser = IncubationCentersSerializer(r, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getraqamlashtirish(request):
    s = Raqamlashtirishxizmalari.objects.all()
    ser = RaqamlashtirishXizmatlariSerializer(s, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Getcontact(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    a = Contact.objects.create(fullname=fullname, phone=phone, text=text, email=email)
    ser = ContactSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
def Getxizmatturi(request):
    u = XizmatTuri.objects.all()
    ser = XizmatTuriSerializer(u, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getxizmatlar(request):
    v = Xizmatlar.objects.all()
    ser = XizmatlarSerializer(v, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Getapplication(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    xizmat = request.POST.get('xizmat')
    xizmat = XizmatTuri.objects.get(id=xizmat)
    b = Application.objects.create(fullname=fullname, phone=phone, text=text, email=email, xizmat=xizmat)
    ser = ApplicationSerializer(b)
    return Response(ser.data)


def Index(request):
    return render(request,'dashboard-school.html')



def Section_funk(request):
    section = Section.objects.all()
    context = {
        'section': section
    }
    return render(request, 'section.html', context)


def Info_funk(request):
    section = Info.objects.all()
    context = {
        'section': section
    }

    return render(request, 'info.html',context)


def Slider_funk(request):
    section = Slider.objects.all()
    context = {
        'section': section
    }

    return render(request, 'slider.html',context)



def Projects_funk(request):
    section = Projects.objects.all()
    context = {
        'section': section
    }

    return render(request, 'project.html', context)




def Technopark_funk(request):
    section = Technopark.objects.all()
    context = {
        'section': section
    }

    return render(request, 'technopark.html', context)



def Postal_Services(request):
    section = Postalservices.objects.all()
    context = {
        'section': section
    }

    return render(request, 'postalservices.html', context)


def Boglanish_Funk(request):
    section = Boglanish.objects.all()
    context = {
        'section': section
    }

    return render(request, 'boglanish.html', context)


def Mobileoperators_Funk(request):
    section = Mobileoperators.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Mobileoperators.html', context)


def Internetproviders_Funk(request):
    section = Internetproviders.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Internetproviders.html', context)


def OurAudience_Funk(request):
    section = OurAudience.objects.all()
    context = {
        'section': section
    }

    return render(request, 'OurAudience.html', context)


def Percentage_Funk(request):
    section = Percentage.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Percentage.html', context)


def Residents_Funk(request):
    section = Residents.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Residents.html', context)


def Team_Funk(request):
    section = Team.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Team.html', context)


def Coimages_Funk(request):
    section = Coimages.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Coimages.html', context)

def Coworking_Funk(request):
    section = Coworking.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Coworking.html', context)


def InfrastructureSlider_Funk(request):
    section = InfrastructureSlider.objects.all()
    context = {
        'section': section
    }

    return render(request, 'InfrastructureSlider.html', context)


def StudyDirections_Funk(request):
    section = StudyDirections.objects.all()
    context = {
        'section': section
    }

    return render(request, 'StudyDirections.html', context)


def ItAcademy_Funk(request):
    section = ItAcademy.objects.all()
    context = {
        'section': section
    }

    return render(request, 'ItAcademy.html', context)


def StartupDirections_Funk(request):
    section = StartupDirections.objects.all()
    context = {
        'section': section
    }

    return render(request, 'StartupDirections.html', context)


def IncubationCenters_Funk(request):
    section = IncubationCenters.objects.all()
    context = {
        'section': section
    }

    return render(request, 'IncubationCenters.html', context)


def Raqamlashtirishxizmalari_Funk(request):
    section = Raqamlashtirishxizmalari.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Raqamlashtirishxizmalari.html', context)


def Contact_Funk(request):
    section = Contact.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Contact.html', context)
    

def XizmatTuri_Funk(request):
    section = XizmatTuri.objects.all()
    context = {
        'section': section
    }

    return render(request, 'XizmatTuri.html', context)
    

def Xizmatlar_Funk(request):
    section = Xizmatlar.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Xizmatlar.html', context)



def Application_Funk(request):
    section = Application.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Application.html', context)