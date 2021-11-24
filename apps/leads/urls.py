from django.urls import path

from apps.leads.views import lead_list, lead_detail, create_lead, update_lead, delete_lead,\
    LeadDetailView, LeadCreateView

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead_list'),
    #path('<int:pk>/', lead_detail, name='detail'),
    path('<int:pk>', LeadDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', update_lead, name='update'),
    path('<int:pk>/delete/', delete_lead, name='delete'),
    #path('create/', create_lead, name='create'),
    path('create/', LeadCreateView.as_view(), name='create'),

]