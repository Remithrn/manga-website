from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='home'),
    path('create/',views.create,name='create'),
    path('detail/<int:id>/',views.details,name='detail'),
    path('update/<int:id>/',views.update_details,name='update'),
    path('delete/<int:id>',views.delete_book,name='delete'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register',views.register_user,name='register'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]
