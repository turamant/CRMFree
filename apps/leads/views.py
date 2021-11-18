from django.shortcuts import render, get_object_or_404, redirect

from apps.leads.forms import LeadForm, LeadModelForm
from apps.leads.models import Lead, Agent


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/list.html', {'leads': leads})

def lead_detail(request, id):
    lead = get_object_or_404(Lead, id=id)
    return render(request, 'leads/detail.html', {'lead': lead})

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

def update_lead(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:list')
    return render(request, 'leads/update.html', {'form': form, 'lead': lead})

def delete_lead(request, id):
    lead = Lead.objects.get(id=id)
    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('leads:list')
        lead.delete()
        return redirect('leads:list')
    return render(request, 'leads/delete.html', {'lead': lead})

def XXXupdate_lead(request, id):
    #lead = get_object_or_404(Lead, id=id)
    lead = Lead.objects.get(id=id)
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
