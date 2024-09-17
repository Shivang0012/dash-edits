from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.urls import reverse
from .models import Job

# Create your views here.
def dash(request):
    jobs=Job.objects.all()
    
    context={
        'jobs':jobs
    }
    return render(request,'dashboard/home.html',context)

def search(request):
    if request.method == "POST":
        searched=request.POST['searched'] 
        jobs=Job.objects.filter(clientname__contains=searched)
        return render(request,'dashboard/search.html',{'searched':searched,'jobs':jobs,})
    
    else:
        return render(request,'dashboard/search.html',{})




def newjobsheet(request):
    if request.method=="POST":
        clientname=request.POST['clientname']
        contact=request.POST['contact']
        rdate=request.POST['rdate']
        inventry=request.POST['inventry']
        image=request.POST['image']
        issue=request.POST['issue']
        cnotes=request.POST['cnotes']
        technician=request.POST['technician']
        amount=request.POST['amount']
        ddate=request.POST['ddate']
        status=request.POST['status']
        if len(clientname)<3 or len(contact)<10 or len(contact)>12 or len(inventry)<3 or len(issue)<3 or len(cnotes)<3 or len(technician)<3 or len(amount)<3 or len(status)<3 :
            # code for printing message. 
            pass
        else:  
            jobsheet=Job(clientname=clientname,contact=contact,rdate=rdate,inventry=inventry,image=image,issue=issue,cnotes=cnotes,technician=technician,amount=amount,ddate=ddate,status=status)
            jobsheet.save()
    return render(request,"dashboard/newjobsheet.html")


def jobdata(request,id):
    person=Job.objects.filter(clientid=id)
    return render(request,"dashboard/jobdata.html",{'person':person[0]})



def editdata(request,myid):
    data=Job.objects.all()
    if request.method=="POST":
            data=Job.objects.get(pk=myid)
            data.clientname=request.POST.get('clientname')
            data.contact=request.POST.get('contact')
            data.rdate=request.POST.get('rdate')
            data.inventry=request.POST.get('inventry')
            data.image=request.POST.get('image')
            data.issue=request.POST.get('issue')
            data.cnotes=request.POST.get('cnotes')
            data.technician=request.POST.get('technician')
            data.amount=request.POST.get('amount')
            data.ddate=request.POST.get('ddate')
            data.status=request.POST.get('status')
            data.save()
            return redirect("/")
            # objct.txt=Job(clientname=clientname,contact=contact,rdate=rdate,inventry=inventry,image=image,issue=issue,cnotes=cnotes,technician=technician,amount=amount,ddate=ddate,status=status)
            # objct.save()
            # return redirect('/')
    else:
        data=Job.objects.get(pk=myid)
        print(data)
        return render(request,"dashboard/editdata.html",{'data':data})
    
def delete(request,myid):
    job=Job.objects.get(clientid=myid)
    job.delete()
    return HttpResponseRedirect(reverse('dash'))
    