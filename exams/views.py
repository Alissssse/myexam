from django.shortcuts import render
from .models import akxam

def akxam_view(request):
    exams = akxam.objects.filter(is_public=True)
    return render(request, 'exams/akxam.html', {'exams': exams})
