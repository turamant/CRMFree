from django.urls import path

from apps.leads.views import lead_list, lead_detail, create_lead, update_lead, delete_lead


app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='list'),
    path('<int:id>/', lead_detail, name='detail'),
    path('<int:id>/update/', update_lead, name='update'),
    path('<int:id>/delete/', delete_lead, name='delete'),
    path('create/', create_lead, name='create'),


]