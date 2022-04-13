from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import tests

admin.site.site_header = "TKD Main Admin"
admin.site.site_title = "TKD Main Admin"
admin.site.index_title = "Welcome to TKD"
urlpatterns = [
    # path('', views.home, name="home"),
    # path('insertdata/', tests.insertdata, name="insertdata"),
    path('passwordlist/', views.passwordlist, name="passwordlist"),
    path('passwordgenerator/', views.passwordgenerator, name="passwordgenerator"),
    # path('csv/', views.csv, name="csv"),
    # path('insertdata/', views.insertdata, name="insertdata"),
    path('mypasswords/', views.PasswordViewSet.as_view()),
    path('detail/', views.MydetailsViewSet.as_view()),
    path('service/', views.MyservicesViewSet.as_view()),
    path('skills/', views.MyskillViewSet.as_view()),
    path('languages/', views.MylanguageViewSet.as_view()),
    path('knowleges/', views.MyknowledgeViewSet.as_view()),
    path('knowleges/', views.MyknowledgeViewSet.as_view()),
    path('social/', views.SocialViewSet.as_view()),
    path('projects/', views.MyprojectViewSet.as_view()),
    path('projects/<int:id>', views.MyprojectViewSet.as_view()),
    path('music/', views.MusicViewSet.as_view()),
    path('icons/', views.MyiconsViewSet.as_view()),
    path('countrys/', views.countrysViewSet.as_view()),
    path('state/', views.StateViewSet.as_view()),
    path('state/<country>', views.StateViewSet.as_view()),
    path('continents/', views.continentsViewSet.as_view()),
    path('currentacy/', views.CurrentacyViewSet.as_view()),
    path('language/', views.LanguageViewSet.as_view()),
    path('friends/', views.MyfriendViewSet.as_view()),
    path('passwordjson/', views.passwordjson.as_view()),
    path('password/<int:lenght>', views.custompassword.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('profileavaterchange/<int:id>', views.profileavaterchange, name="profileavaterchange"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)