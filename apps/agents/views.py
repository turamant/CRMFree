from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.agents.forms import AgentModelForm
from apps.leads.models import Agent



class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    model = Agent

def agent_list(request):
    agents = Agent.objects.all()
    print('...',agents)
    context = {'agents': agents}
    return render(request, 'agents/agent_list.html', context)


#############################################

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
