
from django.urls import path
from . import views



app_name='App_login'

urlpatterns = [
    path("signup/",views.signup,name='signup'),
    
    path("signin/",views.log_in,name='signin'),
    path("log_out/",views.log_out,name='log_out'),
    path("profile/",views.profile,name='profile'),
    path("ChangeProfile/",views.ChangeProfile,name='ChangeProfile'),
    #you have to use by defult route password/
    path("password/",views.changePassword,name='changePassword'),
    path("profilePics/",views.profilePics,name='profilePics'),
    
    
]
# do not include here it should be in Blog 
#urlpatterns+=staticfiles_urlpatterns()
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
