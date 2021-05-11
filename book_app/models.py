from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=200,unique=True)

    def __str__(self):
        return self.firstname+" "+self.lastname

class Sell(models.Model):
    # CHANGE
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    book_name=models.CharField(max_length=200, help_text="Enter the book name")
    author=models.CharField(max_length=200, help_text="Enter the book's author name")
    published_by=models.CharField(max_length=200)
    # tags=models.ManyToManyField('Tag')
    FIRSTHAND='Firsthand'
    SECONDHAND='Secondhand'
    TYPE_CHOICES=[
        ('Firsthand','Firsthand'),
        ('Secondhand','Secondhand'),
    ]
    ACTION='ACTION'
    THRILLER='THRILLER'
    ART='ART'
    ROMANCE='ROMANCE'
    FAIRYTALE='FAIRYTALE'
    TRUE_CRIME='TRUE CRIME'
    DRAMA='DRAMA'
    DIARY='DIARY'
    COMIC='COMIC'
    HISTORY='HISTORY'
    HORROR='HORROR'
    TAG_CHOICES=[
        ('ACTION','Action'),
        ('THRILLER','Thriller'),
        ('ART','Art'),
        ('ROMANCE','Romance'),
        ('FAIRYTALE','Fairytale'),
        ('TRUE CRIME','True_crime'),
        ('DRAMA','Drama'),
        ('DIARY','Diary'),
        ('COMIC','Comic'),
        ('HISTORY','History'),
        ('HORROR','Horror')
    ]
    tags=models.CharField(max_length=20, choices=TAG_CHOICES, default=ACTION)
    types=models.CharField(max_length=30, choices=TYPE_CHOICES, default=SECONDHAND)
    price=models.DecimalField(max_digits=5, decimal_places=2, help_text="Enter the book's price")
    pin_code=models.CharField(max_length=10, help_text="Enter the pincode of your suitable area to sell")
    description=models.TextField(max_length=300, help_text="Please add if any extra info is there for the book", null=True)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    

    def __str__(self):
        return self.book_name+"-"+self.author

class Cart(models.Model):
    seller = models.ForeignKey(Sell, on_delete=models.CASCADE)

