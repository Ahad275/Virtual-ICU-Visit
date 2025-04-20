from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby),
    path('room/<str:room_name>/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    # new
    path('home/', views.home, name='home'),
   path('base/', views.base, name='base'),
   # path('admin_portal/', views.admin_portal, name='admin_portal'),
   path('contact/', views.Contact, name='contact'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('login/', views.login, name='login'),
   path('patient_view/', views.patient_view, name='patient_view'),
   path('register/', views.register, name='register'),
   path('reports/', views.reports, name='reports'),
   path('beds/', views.beds, name='beds'),
   path('prescriptions/', views.prescriptions, name='prescriptions'),
   path('vitals/', views.vitals, name='vitals'),
]