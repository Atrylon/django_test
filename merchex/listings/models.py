from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    def __str__(self) -> str:
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        BLACK_METAL = 'BM'
        DEATH_METAL = 'DM'
        POP = 'POP'
        CLASSIQUE = 'C'
        POP_ROCK = 'PR'

    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(choices=Genre.choices, max_length=5)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active=models.fields.BooleanField(default=True)
    official_page=models.fields.URLField(null=True,blank=True)


class Listing(models.Model):

    def __str__(self) -> str:
        return f'{self.title} - {self.type}'

    class Type(models.TextChoices):
        DISQUES = 'Records'
        PLACE_CONCERT = 'Concert ticket'
        VETEMENTS = 'Clothing'
        AFFICHES = 'Posters'
        DIVERS = 'Miscellaneous'

    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=500)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    type=models.fields.CharField(choices=Type.choices, max_length=50)
    band=models.ForeignKey(Band, null=True,on_delete=models.SET_NULL)
    

