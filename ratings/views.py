from django.shortcuts import render
from .models import Rating,Doc
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/main.html', context)


def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})


class MainView(TemplateView):
    template_name = "ratings/index.html"

def file_upload_view(request):
    print(request.FILES)
    if request.method == "POST":
        my_file = request.FILES.get('file')
        Doc.objects.create(upload=my_file)

        return HttpResponse("uploaded")
    return JsonResponse({"post":'false'})




