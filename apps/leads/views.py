from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from django.core.mail import send_mail

from apps.leads.forms import LeadForm, LeadModelForm, CustomUserCreateForm
from apps.leads.models import Lead, Agent


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreateForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, 'landing.html')

############################################

class LeadListView(generic.ListView):
    queryset = Lead.objects.all()
    template_name = 'leads/list.html'
    context_object_name = 'leads'

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/list.html', {'leads': leads})

###############################################################

class LeadDetailView(generic.DetailView):
    queryset = Lead.objects.all()
    template_name = 'leads/detail.html'
    context_object_name = 'lead'

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    return render(request, 'leads/detail.html', {'lead': lead})

##############################################################

class LeadCreateView(generic.CreateView):
    template_name = 'leads/create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:list')
    
    def form_valid(self, form):
        #TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com", "tur@tur.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

def create_lead(request):
    form = LeadModelForm()
    print(request.POST)
    if request.method == 'POST':
        print('Receive a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("форма валидная")
            print(form.cleaned_data)
            print(form.cleaned_data['age'])
            form.save()
            print("Lead created!")
            return redirect('leads:list')
    return render(request, 'leads/create.html', {'form': form})

#############################################################

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:list')

def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:list')
    return render(request, 'leads/update.html', {'form': form, 'lead': lead})

#############################################################################

class LeadDeleteView(generic.DetailView):
    template_name = 'leads/delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:list')


def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('leads:list')
        lead.delete()
        return redirect('leads:list')
    return render(request, 'leads/delete.html', {'lead': lead})

def XXXupdate_lead(request, pk):
    #lead = get_object_or_404(Lead, id=pk)
    lead = Lead.objects.get(id=pk)
    form = LeadForm()
    print(request.POST)
    if request.method == 'POST':
        print('Receive a post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print("форма валидная")
            print(form.cleaned_data)
            print(form.cleaned_data['age'])
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']

            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.save()

            print("Lead created!")
            return redirect('leads:list')
    return render(request, 'leads/update.html', {'form': form, 'lead': lead})



def XXXcreate_lead(request):
    form = LeadForm()
    print(request.POST)
    if request.method == 'POST':
        print('Receive a post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print("форма валидная")
            print(form.cleaned_data)
            print(form.cleaned_data['age'])
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent,
            )
            print("Lead created!")
            return redirect('leads:list')
    return render(request, 'leads/create.html', {'form': form})
