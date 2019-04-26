from django.shortcuts import render,HttpResponse

# Create your views here.
def index_views(request):
    return render(request,'index.html')

def header_views(request):
    return render(request,"header.html")
def footer_views(request):
    return render(request, "footer.html")