from .models import *
from rest_framework import serializers

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        
class TechnoparkSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Technopark
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class PostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postalservices
        fields = "__all__"

class BoglanishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boglanish
        fields = "__all__"

class MobileoperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobileoperators
        fields = "__all__"

class InternetprovidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internetproviders
        fields = "__all__"

class OurAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAudience
        fields = "__all__"

class PercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percentage
        fields = "__all__"

class ResidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residents
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class CoimagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coimages
        fields = "__all__"

class CoworkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coworking
        fields = "__all__"

class InfrastructureSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureSlider
        fields = "__all__"

class StudydirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDirections
        fields = "__all__"

class ItAcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItAcademy
        fields = "__all__"

class StartupDirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupDirections
        fields = "__all__"

class IncubationCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncubationCenters
        fields = "__all__"

class RaqamlashtirishXizmatlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raqamlashtirishxizmalari
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class XizmatTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = XizmatTuri
        fields = "__all__"

class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
