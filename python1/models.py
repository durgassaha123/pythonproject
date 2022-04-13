from django.db import models
import computed_property
import os
import random
import datetime

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

CatagoryChoices = [
    ['software', 'software'],
    ['website', 'website'],
    ['project', 'project'],
    ['game', 'game'],
    ['list', 'list'],
]

class passwords(models.Model):
    email = models.EmailField(default="thekoushikdurgas@gmail.com")
    link = models.URLField(max_length=200,default="http://google.com")
    username = models.CharField(max_length=200,default="thekoushikdurgas")
    subject = models.CharField(max_length=200,default="thekoushikdurgas")
    password = models.CharField(max_length=200,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.link
    class Meta:
        db_table = "passwordlist" 
        
class social(models.Model):
    title = models.CharField(max_length=200,default="thekoushikdurgas")
    title1 = models.CharField(max_length=200,default="thekoushikdurgas")
    icon = models.CharField(max_length=200,default="thekoushikdurgas")
    link = models.URLField(max_length=200,default="http://google.com")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "sociallist" 
        
class mydetails(models.Model):
    title = models.CharField(max_length=2000,default="thekoushikdurgass")
    subject = models.CharField(max_length=200,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title 
    class Meta:
        db_table = "mydetailslist" 
        
class myskills(models.Model):
    title = models.CharField(max_length=200,default="thekoushikdurgas")
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def degdef(self):
        return (self.value * 360)/100
    deg = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degdef',default="0")
    @property
    def degrdef(self):
        k=(self.value * 360)/100
        return k if (k <= 180) else 180
    degr = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degrdef',default="0")
    @property
    def degldef(self):
        k=(self.value * 360)/100
        return 0 if (k <= 180) else (k-180)
    degl = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degldef',default="0")
    def __str__(self):
        return self.title 
    class Meta:
        db_table = "myskilllist" 
        
class mylanguage(models.Model):
    title = models.CharField(max_length=200,default="thekoushikdurgas")
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def degdef(self):
        return (self.value * 360)/100
    deg = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degdef',default="0")
    @property
    def degrdef(self):
        k=(self.value * 360)/100
        return k if (k <= 180) else 180
    degr = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degrdef',default="0")
    @property
    def degldef(self):
        k=(self.value * 360)/100
        return 0 if (k <= 180) else (k-180)
    degl = computed_property.ComputedDecimalField(max_digits=100, decimal_places=2, compute_from='degldef',default="0")
    def __str__(self):
        return self.title 
    class Meta:
        db_table = "mylanguagelist"   
        
class myknowledge(models.Model):
    title = models.CharField(max_length=200,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title 
    class Meta:
        db_table = "myknowledgelist"         
        
class myservices(models.Model):
    icon = models.CharField(max_length=200,default="thekoushikdurgas")
    name = models.CharField(max_length=200,default="thekoushikdurgas")
    desc = models.CharField(max_length=200,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    class Meta:
        db_table = "myserviceslist" 
        
def myprojectpath(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'myproject/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)

class myproject(models.Model):
    title = models.CharField(max_length=200,default="thekoushikdurgas")
    myprojectpic = models.ImageField(upload_to=myprojectpath, blank=True, null=True, default='myproject/default.jpg')
    name = models.CharField(max_length=200,default="thekoushikdurgas")
    category = models.CharField(choices=CatagoryChoices, default="all", max_length=150)
    desc = models.CharField(max_length=20000,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def project_d(self):
        if (len(list(myproject.objects.filter(name=self.name).values())) == 0):
            time = datetime.datetime.now()
            return time.strftime("%d %b %Y")
        else:
            time = datetime.datetime.strptime(str(list(myproject.objects.filter(name=self.name).values())[0]['created_at'])[:10],'%Y-%m-%d')
            return time.strftime("%d %b %Y")
    projectd = computed_property.ComputedCharField(max_length=150, compute_from='project_d',default="0")
    def __str__(self):
        return self.name 
    class Meta:
        db_table = "myprojectlist" 
        
def myfriendpath(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'myfriend/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)

class myfriend(models.Model):
    name = models.CharField(max_length=200,default="thekoushikdurgas")
    myprojectpic = models.ImageField(upload_to=myfriendpath, blank=True, null=True, default='myfriend/default.jpg')
    facebook = models.URLField(max_length=200,default="https://www.facebook.com/")
    twitter = models.URLField(max_length=200,default="https://twitter.com/")
    linkedin = models.URLField(max_length=200,default="https://www.linkedin.com/in/")
    instagram = models.URLField(max_length=200,default="https://www.instagram.com/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    class Meta:
        db_table = "myfriendlist" 
        
def mymusicpath1(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'mymusic/pic/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)

def mymusicpath2(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'mymusic/audio/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)

LaguageChoices = [
    ['hindi', 'hindi'],
    ['bengali', 'bengali'],
    ['english', 'english'],
]

audiotype = [
    ['music', 'music'],
    ['story', 'story'],
]        
class mymusic(models.Model):
    title= models.CharField(max_length=200,default="thekoushikdurgas")
    artist= models.CharField(max_length=200,default="thekoushikdurgas")
    image= models.ImageField(upload_to=mymusicpath1, blank=True, null=True, default='mymusic/pic/default.jpg',max_length=2000)
    audio_file = models.FileField(upload_to=mymusicpath2, blank=True, null=True, default='mymusic/audio/default.mp3',max_length=2000)
    audio_link = models.URLField(max_length=200,default="https://www.youtube.com/")
    language = models.CharField(choices=LaguageChoices, default="bengali", max_length=150)
    typeaudio = models.CharField(choices=audiotype, default="music", max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title 
    class Meta:
        db_table = "mymusiclist" 

class myicons(models.Model):
    link = models.CharField(max_length=3000)
    name = models.CharField(max_length=3000)
    title = models.CharField(max_length=3000)
    csscontentcode = models.CharField(max_length=3000)
    svglink = models.CharField(max_length=3000)
    icontype = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "myiconslist"
        
class countrys(models.Model):
    ccode = models.CharField(max_length=30,default="thekoushikdurgas")
    value = models.CharField(max_length=30,default="thekoushikdurgas")
    name = models.CharField(max_length=30,default="thekoushikdurgas")
    mcode = models.CharField(max_length=30,default="thekoushikdurgas")
    continents = models.CharField(max_length=30,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "countrys"
        
class state(models.Model):
    state= models.CharField(max_length=3000,default="thekoushikdurgas")
    countrys = models.CharField(max_length=30,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.state
    class Meta:
        db_table = "state"
        
class continents(models.Model):
    ccode = models.CharField(max_length=30,default="thekoushikdurgas")
    name = models.CharField(max_length=30,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "continents"
        
class currentacy(models.Model):
    symbol = models.CharField(max_length=30,default="thekoushikdurgas")
    name = models.CharField(max_length=30,default="thekoushikdurgas")
    symbolnative = models.CharField(max_length=30,default="thekoushikdurgas")
    decimaldigits = models.CharField(max_length=30,default="thekoushikdurgas")
    rounding = models.CharField(max_length=30,default="thekoushikdurgas")
    code = models.CharField(max_length=30,default="thekoushikdurgas")
    nameplural = models.CharField(max_length=30,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code
    class Meta:
        db_table = "currentacy"
        
class language(models.Model):
    code = models.CharField(max_length=30,default="thekoushikdurgas")
    name = models.CharField(max_length=30,default="thekoushikdurgas")
    nativeName = models.CharField(max_length=30,default="thekoushikdurgas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code
    class Meta:
        db_table = "language"
        
# class mainsub(models.Model):
#     subid = models.CharField(max_length=30)
#     name= models.CharField(max_length=3000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table = "mainsub"
        
# class secsub(models.Model):
#     subid = models.CharField(max_length=30)
#     mainsub = models.CharField(max_length=30)
#     name= models.CharField(max_length=3000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table = "secsub"