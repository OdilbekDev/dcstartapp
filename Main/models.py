from django.db import models

# Create your models here.
# umumiy hamma page ni boshida
class Info(models.Model):
    logo = models.ImageField(upload_to="Logo/")
    short_phone = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    address_uz = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    address_en = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

    

# asosiy paga boshlanishi
class Slider(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    video = models.FileField(upload_to="Videos/")


class Projects(models.Model):
    image = models.ImageField(upload_to="Projects/")
    text_uz = models.TextField()
    text_en = models.TextField()
    text_ru = models.TextField()


class Technopark(models.Model):
    icon = models.ImageField(upload_to="Texnopark/")
    text_uz = models.CharField(max_length=100)
    text_ru = models.CharField(max_length=100)
    text_en = models.CharField(max_length=100)
    number = models.IntegerField()


class Section(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    image = models.ImageField(upload_to="Sections/")


class Postalservices(models.Model):
    logo = models.ImageField(upload_to="Pochta xizmatlari/")


class Boglanish(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    text = models.CharField(max_length=255)


class Mobileoperators(models.Model):
    logo = models.ImageField(upload_to="Mobile operators/")


class Internetproviders(models.Model):
    logo = models.ImageField(upload_to="Internet providers/")


class OurAudience(models.Model):
    image = models.ImageField(upload_to="OurAudience/")
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()

class Percentage(models.Model):
    percent = models.FloatField()
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

class Residents(models.Model):
    image = models.ImageField(upload_to="Residents/")
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)



class Team(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    image = models.ImageField(upload_to="Team/")


class Coimages(models.Model):
    image = models.ImageField(upload_to="Coworking images/")


class Coworking(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    image = models.ManyToManyField(Coimages)


class InfrastructureSlider(models.Model):
    image = models.ImageField(upload_to="InfrastructureSlider")
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()

class StudyDirections(models.Model):
    image = models.ImageField(upload_to="StudyDirections/")
    tittle_uz = models.CharField(max_length=255)
    tittle_ru = models.CharField(max_length=255)
    tittle_en = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()

class ItAcademy(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    texnologies = models.TextField()
    duration = models.CharField(max_length=50)
    start = models.DateField()
    image = models.ImageField(upload_to="It Academy/")


class StartupDirections(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="StartupDirections/")


class IncubationCenters(models.Model):
    icon = models.ImageField(upload_to="IncubationCenters")
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)


class Raqamlashtirishxizmalari(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Raqamlashtirishxizmalari/")
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()


class XizmatTuri(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    price = models.IntegerField()



class Xizmatlar(models.Model):
    xizmat = models.ForeignKey(XizmatTuri, on_delete=models.PROTECT)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

class Application(models.Model):
    xizmat = models.ForeignKey(XizmatTuri, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()