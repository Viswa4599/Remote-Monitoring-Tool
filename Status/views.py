from django.shortcuts import render
from Status.models import CPU,Network,RAM,Clock
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView
#from chartjs.views.lines import BaseLineChartView

@csrf_exempt
def status_view(request):

    if(request.method == 'POST'):
        time_ = request.POST.get('datetime')
        percent_ = float(request.POST.get('cpu - percent','-1'))
        user_times_ = float(request.POST.get('cpu - user times','-1'))
        temperature_ = int(request.POST.get('cpu - temperature','-1'))
        total_ = int(request.POST.get('virtual memory - total','-1'))
        ram_percent = float(request.POST.get('virtual memory - percent','-1'))
        sent_ = int(request.POST.get('network - bytes sent','-1'))
        received_ = int(request.POST.get('network - bytes received','-1'))
        t = Clock.objects.create(time = time_)
        t.save()
        c = CPU.objects.create(percent = percent_,user_times = user_times_, temperature=temperature_)
        c.save()
        r = RAM.objects.create(percent = ram_percent,total = total_)
        r.save()
        n = Network.objects.create(sent = sent_,received = received_)
        n.save()

    cpu_percent = list(CPU.objects.values_list('percent', flat=True))
    ram_percent_ = list(RAM.objects.values_list('percent',flat = True))
    net_sent = list(Network.objects.values_list('sent',flat = True))
    net_received = list(Network.objects.values_list('sent',flat = True))
    clock = list(Clock.objects.values_list('time',flat = True))

   # sys ={"cpu_percent": cpu_percent,"ram_percent": ram_percent,"net_sent": net_sent,"sys_time":clock,"net_received":net_received}

    #return render(request,template_name='status.html')
    cpu_graph=[]
    ram_graph=[]
    sent_graph=[]
    received_graph=[]
    for i in range(len(cpu_percent)):
        cpu_graph.append([cpu_percent[i],clock[i]])
        ram_graph.append([ram_percent_[i],clock[i]])
        sent_graph.append([net_sent[i],clock[i]])
        received_graph.append([net_received[i],clock[i]])

    return JsonResponse(data ={'cpu_graph':cpu_graph,'ram_graph':ram_graph,'sent':sent_graph,'received':received_graph},safe = False)
    #"ram_percent": ram_percent,"net_sent": net_sent,"sys_time":clock,"net_received":net_received})

@csrf_exempt
def sample_view(request):
    return render(request,template_name='status.html')