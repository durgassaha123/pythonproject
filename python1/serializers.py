from rest_framework import routers, serializers, viewsets
from .models import passwords,mydetails,myservices,myskills,mylanguage,myknowledge,social,myproject,myfriend,mymusic,myicons,countrys,state,continents,currentacy,language
# Serializers define the API representation.
class PasswordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = passwords
        fields = ['id','link','email','username','subject','password','created_at','updated_at']
        
class MydetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mydetails
        fields = ['id','title','subject','created_at','updated_at'] 
        
class MyskillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myskills
        fields = ['id','title','value','deg','degr','degl','created_at','updated_at']      
          
class MylanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mylanguage
        fields = ['id','title','value','deg','degr','degl','created_at','updated_at']      
          
class MyknowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myknowledge
        fields = ['id','title','created_at','updated_at']      
          
class MyservicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myservices
        fields = ['name','icon','desc','created_at','updated_at']
          
class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = social
        fields = ['id','title','title1','icon','link','created_at','updated_at']
          
class MyprojectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myproject
        fields = ['id','name','title','category','desc','myprojectpic','projectd','created_at','updated_at']
          
class MyfriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myfriend
        fields = ['id','name','myprojectpic','facebook','twitter','linkedin','instagram','created_at','updated_at']
          
class MymusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mymusic
        fields = ['id','title','artist','image','audio_file','audio_link','language','typeaudio','created_at','updated_at']
        
class MyiconsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myicons
        fields = ['id','link','name','title','csscontentcode','svglink','icontype','created_at','updated_at']
        
class countrysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = countrys
        fields = ['id','ccode','value','name','mcode','continents','created_at','updated_at']
        
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = state
        fields = ['id','state','countrys','created_at','updated_at']
        
class continentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = continents
        fields = ['id','ccode','name','created_at','updated_at']
        
class CurrentacySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = currentacy
        fields = ['id','symbol','name','symbolnative','decimaldigits','rounding','code','nameplural','created_at','updated_at']
        
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = language
        fields = ['id','code','name','nativeName','created_at','updated_at']