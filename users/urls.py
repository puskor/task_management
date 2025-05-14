
from django.urls import path
from users.views import sign_up,sign_in,sign_out,activate_user,admin_dashboard,assign_role,create_group,group_list,CustomSign_in,Profile_view,Change_password,Password_reset_view,Password_reset_confirm_view
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView
from django.views.generic.base import TemplateView
urlpatterns = [
    path("sign_up/",sign_up,name="sign-up"),
    # path("sign_in/",sign_in,name="sign_in"),
    path("sign_in/",LoginView.as_view(template_name = 'registrations/sign_in.html'),name="sign_in"),
    
    # path("sign_out/",sign_out,name="sign_out"),
    path("sign_out/",LogoutView.as_view(),name="sign_out"),
    
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/',admin_dashboard,name="admin-dashboard"),
    path("admin/<int:user_id>/assign_role/",assign_role,name="assign_role"),
    path("admin/create_group/",create_group,name="create_group"),
    path("admin/group_list/",group_list,name="group_list"),
    path("profile/",Profile_view.as_view(template_name = "account/profile.html"),name="profile"),
    path("password_change/",Change_password.as_view(template_name="account/password_change.html"),name="password_change"),
    path("password_change_done/",PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name="password_change_done"),
    path("password_reset/",Password_reset_view.as_view(),name="password_reset"),
    path("password_confirm_reset/<uidb64>/<token>/",Password_reset_confirm_view.as_view(),name="password_reset_confirm"),
    
]
