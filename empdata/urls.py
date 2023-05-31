from django.urls import path
from . import views
urlpatterns=[
    path('form/',views.submit,name='submit'),
    path('home/',views.home,name='home'),
    path('display/',views.reg_page,name='display'),
    path('login',views.render_login,name='login'),
    path('success/',views.success,name='success'),
    path('prompt/',views.reg_prompt,name='prompt'),
    path('passcheck/',views.det,name='passcheck'),
    #path('welcome/',views.welcome,name='Welcome'),
]