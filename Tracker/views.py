from django.shortcuts import redirect
from .forms import TrackerForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Tracker
from django.http import HttpResponse
import csv
from django.db.models import Q

def tracker_list(request):

#    if not request.user.is_authenticated:
#        return render(request, 'registration/login.html')
#    else:
#        posts = Tracker.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        latest_tracker_list = Tracker.objects.order_by('-created_date')[:20]
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'tracker/tracker_list.html', context)


def tracker_new(request):
    if request.method == "POST":
        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_detail', pk=tracker.pk)

    else:
        form = TrackerForm
        return render(request, 'tracker/tracker_edit.html', {'form': form})

def tracker_detail(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    return render(request, 'tracker/tracker_detail.html', {'tracker': tracker})

def tracker_edit(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == "POST":
        form = TrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_detail', pk=tracker.pk)
    else:
        form = TrackerForm(instance=tracker)
    return render(request, 'tracker/tracker_edit.html', {'form': form})

def tracker_edit1(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == "POST":
        form = TrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_detail', pk=tracker.pk)
    else:
        form = TrackerForm(instance=tracker)
    return render(request, 'tracker/tracker_edit.html', {'form': form})


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="document.csv"'

    writer = csv.writer(response)
    writer.writerow(['Created_Date','UserName','cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Cic_Engineer', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity'])

    latest_tracker_list1 = Tracker.objects.order_by('-created_date')[:10]
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.admin,item.cascade, item.Technology, item.Type, item.Bandwidth_Checked_From_LSM, item.Market, item.eNB, item.LSM, item.CSMS, item.FE_Name, item.Mode_of_Communication,  item.Cic_Engineer, item.Activity_status, item.Site_Status_pre_Activity, item.Site_Status_post_Activity])

    return response

def Calc_link(request):

    return render(request, 'tracker/Calc_link.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query)

            results = Tracker.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'tracker/search.html', context)

        else:
            return render(request, 'tracker/search.html')

    else:
        return render(request, 'tracker/search.html')


def about(request):
    return render(request, 'tracker/about.html')
