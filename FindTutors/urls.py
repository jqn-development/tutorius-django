from django.urls import path
from django.conf.urls import url

from . import views
from tutorius import settings
from django.conf.urls.static import static

app_name = 'FindTutors'

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='signup'),
    path('tutors/', views.Tutors, name='tutors'),
    path('tutees/', views.Tutees, name='tutees'),
    path('register_tutor/', views.TutorRegisterView.as_view(), name='tutor_register'),
    path('register_tutee/', views.TuteeRegisterView.as_view(), name='tutee_register'),
    path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.editprofile, name='edit_profile'),
    path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
