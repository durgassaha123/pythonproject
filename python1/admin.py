from django.contrib import admin
from .models import passwords,mydetails,myservices,myskills,mylanguage,myknowledge,social,myproject,myfriend,mymusic,myicons,countrys,state,continents,currentacy,language

class passwordsAdmin(admin.ModelAdmin):
    list_display = ['id','link','email','username','subject','password','created_at','updated_at']
    list_filter = ['link','created_at','updated_at']
    list_editable = ['email','username','subject','password']
    search_fields = ['email','username','subject','password',]
admin.site.register(passwords,passwordsAdmin)

class mydetailsAdmin(admin.ModelAdmin):
    list_display = ['id','title','subject','created_at','updated_at']
    list_filter = ['title','created_at','updated_at']
    list_editable = ['title','subject']
    search_fields = ['title','subject']
admin.site.register(mydetails,mydetailsAdmin)

class myskillsAdmin(admin.ModelAdmin):
    list_display = ['id','title','value','deg','degr','degl','created_at','updated_at']
    list_filter = ['title','created_at','updated_at']
    list_editable = ['title','value']
    search_fields = ['title','value']
admin.site.register(myskills,myskillsAdmin)

class mylanguageAdmin(admin.ModelAdmin):
    list_display = ['id','title','value','deg','degr','degl','created_at','updated_at']
    list_filter = ['title','created_at','updated_at']
    list_editable = ['title','value']
    search_fields = ['title','value']
admin.site.register(mylanguage,mylanguageAdmin)

class myknowledgeAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at','updated_at']
    list_filter = ['created_at','updated_at']
    list_editable = ['title']
    search_fields = ['title']
admin.site.register(myknowledge,myknowledgeAdmin)

class myservicesAdmin(admin.ModelAdmin):
    list_display = ['id','name','icon','desc','created_at','updated_at']
    list_filter = ['name','created_at','updated_at']
    list_editable = ['name','icon','desc']
    search_fields = ['name','icon','desc']
admin.site.register(myservices,myservicesAdmin)

class socialAdmin(admin.ModelAdmin):
    list_display = ['id','title','title1','icon','link','created_at','updated_at']
    list_filter = ['title','created_at','updated_at']
    list_editable = ['title','title1','icon','link']
    search_fields = ['title','title1','icon','link']
admin.site.register(social,socialAdmin)

class myprojectAdmin(admin.ModelAdmin):
    list_display = ['id','name','title','category','desc','myprojectpic','projectd','created_at','updated_at']
    list_filter = ['title','name','category','desc','created_at','updated_at']
    list_editable = ['title','name','category','desc']
    search_fields = ['title','name','category','desc']
admin.site.register(myproject,myprojectAdmin)

class myfriendAdmin(admin.ModelAdmin):
    list_display = ['id','name','myprojectpic','facebook','twitter','linkedin','instagram','created_at','updated_at']
    list_filter = ['name','created_at','updated_at']
    list_editable = ['name','facebook','twitter','linkedin','instagram']
    search_fields = ['name','facebook','twitter','linkedin','instagram']
admin.site.register(myfriend,myfriendAdmin)

class mymusicAdmin(admin.ModelAdmin):
    list_display = ['id','title','artist','image','audio_file','audio_link','language','typeaudio','created_at','updated_at']
    list_filter = ['language','typeaudio','created_at','updated_at']
    list_editable = ['title','artist','image','audio_file','audio_link','language','typeaudio']
    search_fields = ['title','artist','image','audio_file','audio_link','language','typeaudio']
admin.site.register(mymusic,mymusicAdmin)

class myiconsAdmin(admin.ModelAdmin):
    list_display = ['id','link','name','title','csscontentcode','svglink','icontype','created_at','updated_at']
    list_filter = ['icontype','created_at','updated_at']
    list_editable = ['link','name','title','csscontentcode','svglink','icontype']
    search_fields = ['link','name','title','csscontentcode','svglink','icontype']
admin.site.register(myicons,myiconsAdmin)

class countrysAdmin(admin.ModelAdmin):
    list_display = ['id','ccode','value','name','mcode','continents','created_at','updated_at']
    list_filter = ['continents','created_at','updated_at']
    list_editable = ['ccode','value','name','mcode']
    search_fields = ['ccode','value','name','mcode']
admin.site.register(countrys,countrysAdmin)

class stateAdmin(admin.ModelAdmin):
    list_display = ['id','state','countrys','created_at','updated_at']
    list_filter = ['countrys','created_at','updated_at']
    list_editable = ['state','countrys']
    search_fields = ['state','countrys']
admin.site.register(state,stateAdmin)

class continentsAdmin(admin.ModelAdmin):
    list_display = ['id','ccode','name','created_at','updated_at']
    list_filter = ['created_at','updated_at']
    list_editable = ['ccode','name']
    search_fields = ['ccode','name']
admin.site.register(continents,continentsAdmin)

class currentacyAdmin(admin.ModelAdmin):
    list_display = ['id','symbol','name','symbolnative','decimaldigits','rounding','code','nameplural','created_at','updated_at']
    list_filter = ['created_at','updated_at']
    list_editable = ['symbol','name','symbolnative','decimaldigits','rounding','code','nameplural']
    search_fields = ['symbol','name','symbolnative','decimaldigits','rounding','code','nameplural']
admin.site.register(currentacy,currentacyAdmin)

class languageAdmin(admin.ModelAdmin):
    list_display = ['id','code','name','nativeName','created_at','updated_at']
    list_filter = ['created_at','updated_at']
    list_editable = ['code','name','nativeName']
    search_fields = ['code','name','nativeName']
admin.site.register(language,languageAdmin)

# class mainsubAdmin(admin.ModelAdmin):
#     list_display = ['id','subid','name','created_at','updated_at']
#     list_filter = ['created_at','updated_at']
#     list_editable = ['subid','name']
#     search_fields = ['subid','name']
# admin.site.register(mainsub,mainsubAdmin)

# class secsubAdmin(admin.ModelAdmin):
#     list_display = ['id','subid','mainsub','name','created_at','updated_at']
#     list_filter = ['mainsub','created_at','updated_at']
#     list_editable = ['subid','mainsub','name']
#     search_fields = ['subid','mainsub','name']
# admin.site.register(secsub,secsubAdmin)