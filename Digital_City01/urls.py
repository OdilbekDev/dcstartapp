from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-info/', Getinfo),
    path('get-slider/', Getslider),
    path('get-projects/', Getprojects),
    path('get-technopark/', Gettechnopark),
    path('get-section/<int:pk>/', Getsection),
    path('get-postalservices/', Getpostal),
    path('get-boglanish', Getboglanish),
    path('get-mobileoperators/', Getmobileoperators),
    path('get-internetproviders/', Getinternetproviders),
    path('get-ouraudience/', Getouraudience),
    path('get-percentage/', Getpercentage),
    path('get-residents/', Getresidents),
    path('get-team/', Getteam),
    path('get-coimages/', Getcoimages),
    path('get-coworking/', Getcoworking),
    path('get-infrastructure/', Getinfrastructure),
    path('get-studydirections/', Getstudydirections),
    path('get-itacademy/', Getitacademy),
    path('get-startupdirections/', Getstartupdirections),
    path('get-incubationcenters/', Getincubationcenters),
    path('get-raqamlashtirishxizmatlari/', Getraqamlashtirish),
    path('post-contact/', Getcontact),
    path('get-xizmatturi/', Getxizmatturi),
    path('get-xizmatlar/', Getxizmatlar),
    path('get-application', Getapplication),
    #### 
    path('', Index, name='index'),
    path('section/', Section_funk, name='Section'),
    path('info/',Info_funk,name='info'),
    path('slider/', Slider_funk,name='Slider'),
    path('project/', Projects_funk,name='Project'),
    path('technopark/', Technopark_funk,name='Technopark'),
    path('postalservices/', Postal_Services,name='PostalServices'),
    path('boglanish/', Boglanish_Funk,name='Boglanish'),
    path('mobileoperators/', Mobileoperators_Funk,name='Mobileoperators'),
    path('internetproviders/', Internetproviders_Funk,name='Internetproviders'),
    path('ourAudience/', OurAudience_Funk,name='OurAudience'),
    path('percentage/', Percentage_Funk,name='Percentage'),
    path('residents/', Residents_Funk,name='Residents'),
    path('team/', Team_Funk,name='Team'),
    path('coimages/', Coimages_Funk,name='Coimages'),
    path('coworking/', Coworking_Funk,name='Coworking'),
    path('InfrastructureSlider/', InfrastructureSlider_Funk,name='InfrastructureSlider'),
    path('studyDirections/', StudyDirections_Funk,name='StudyDirections'),
    path('itAcademy/', ItAcademy_Funk,name='ItAcademy'),
    path('startupDirections/', StartupDirections_Funk,name='StartupDirections'),
    path('IncubationCenters/', IncubationCenters_Funk,name='IncubationCenters'),
    path('contact/', Contact_Funk,name='Contact'),
    path('xizmatTuri/', XizmatTuri_Funk,name='XizmatTuri'),
    path('xizmatlar/', Xizmatlar_Funk,name='Xizmatlar'),
    path('application/', Application_Funk,name='Application'),
    path('raqamlashtirishxizmatlari/', Raqamlashtirishxizmalari_Funk,name='Raqamlashtirishxizmatlari'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)