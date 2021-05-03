from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('help',views.help,name='help'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('reg',views.reg,name='reg'),
    path('career',views.career,name='career'),
    path('careertest',views.careertest,name='careertest'),
    path('earnings',views.earnings,name='earnings'),
     path('careertool',views.careertool,name='careertool')
]
