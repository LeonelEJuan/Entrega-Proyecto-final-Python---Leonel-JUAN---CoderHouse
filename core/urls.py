from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  #  inicio tipo landing
    path('blog/', views.page_list, name='page_list'),  #  lista de blogs
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    path('registro/', views.register_ceo, name='register_ceo'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('crear-pagina/', views.create_page, name='create_page'),
    path('editar/<int:page_id>/', views.edit_page, name='edit_page'),
    path('eliminar/<int:page_id>/', views.delete_page, name='delete_page'),
    path('solicitud-reclutamiento/', views.recruitment_request_view, name='recruitment_request'),
]
