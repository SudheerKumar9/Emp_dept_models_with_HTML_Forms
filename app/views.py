from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_department(request):
    if request.method=='POST':
        dn=request.POST['dn']
        dnam=request.POST['dnam']
        dlo=request.POST['dlo']
        DO=Department.objects.get_or_create(dno=dn,dname=dnam,dloc=dlo)[0]
        DO.save()

        return HttpResponse('<center><h1>Insertion of Department Data is Successful</h1></center>')

    return render(request,'insert_department.html')

def insert_employee(request):
    LDO=Department.objects.all()
    d={'LDO':LDO}
    if request.method=='POST':
        dn=request.POST['dn']
        en=request.POST['en']
        enam=request.POST['enam']
        ej=request.POST['ej']
        esl=request.POST['esl']
        DO=Department.objects.get(dno=dn)
        EO=Employee.objects.get_or_create(dno=DO,eno=en,ename=enam,ejob=ej,esal=esl)[0]
        EO.save()

        return HttpResponse('<center><h1>Insertion of Employee Data is Successful</h1></center>')

    return render(request,'insert_employee.html',d)

def retrieve_employee(request):
    LRO=Department.objects.all()
    s={'LRO':LRO}
    if request.method=='POST':
        DOS=request.POST.getlist('dn')
        RDOS=Department.objects.none()
        for i in DOS:
            RDOS=RDOS|Department.objects.filter(dno=i)
        s1={'RDOS':RDOS}
        return render(request,'display_employee.html',s1)

    return render(request,'retrieve_employee.html',s)
