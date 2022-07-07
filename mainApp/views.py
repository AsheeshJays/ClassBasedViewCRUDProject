from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView
from .models import Employee
from .forms import EmployeeRegistration
from django.views import View


class AddShow(TemplateView):
    template_name = 'add&show.html'

    def post(self, request):
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            empID = fm.cleaned_data['empID']
            empName = fm.cleaned_data['empName']
            empDesgination = fm.cleaned_data['empDesgination']
            empSalary = fm.cleaned_data['empSalary']
            reg = Employee(empID=empID,empName=empName,empDesgination=empDesgination,empSalary=empSalary)
            fm.save()
        return HttpResponseRedirect('/')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = EmployeeRegistration()
        emp = Employee.objects.all()
        context = {'form':fm,'employee':emp}
        return context 

class DeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Employee.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UserUpdateView(View):
    def get(self, request, id):
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
        return render(request, 'update.html',{'form':fm})
    def post(self, request, id):
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'update.html',{'form':fm})