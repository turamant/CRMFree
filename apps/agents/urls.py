from django.urls import path

from apps.agents.views import AgentListView, agent_list, AgentCreateView

app_name = 'agents'

urlpatterns = [
    #path('', AgentListView.as_view(), name='agent_list'),
    path('', agent_list, name='agent_list'),
    path('create/', AgentCreateView.as_view(), name='agent_create'),
]