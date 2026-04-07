from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contactus',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('courses',views.courses,name='courses'),
    path('registration',views.register,name='registration'),
    # path('getstates',views.get_states,name='get_states'),
    # path('getcity',views.get_city,name='get_city'),
    path('studentlogin',views.login,name='studentlogin'),
    path('firstlogin',views.firstlogin,name='firstlogin'),
    path('forgetpassword',views.firstlogin,name='forgetpassword'),
    path('otpverify',views.verify_otp,name='otpverify'),
    path('setpassword',views.set_pass,name='setpassword'),
    path('resendotp', views.resend_otp, name='resend_otp'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('studentlogin',views.logout,name='studentlogin'),
    path('course_search',views.course_search,name='course_search'),
    path('my_course',views.my_course,name='my_course'),
    path('enrollnow/<id>',views.enroll),
    path('cancelenroll/<id>',views.cancelenroll),
    path('password_update',views.pass_update,name='password_update'),
    
]