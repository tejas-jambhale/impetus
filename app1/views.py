from django.shortcuts import render

# Create your views here.
def page1(request):
    
        return render(request, 'page1.html', {})


def page2(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        search_query1 = request.GET.get('search_box1', None)
        search_query2 = request.GET.get('search_box2', None)
        pic = request.GET.get('pic')
        return render(request, 'page2.html', {"search_box": search_query,"search_box1": search_query1,"search_box2": search_query2})

def page5(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        search_query1 = request.GET.get('search_box1', None)
        search_query2 = request.GET.get('search_box2', None)
        pic = request.GET.get('pic')
        return render(request, 'page5.html', {"search_box": search_query,"search_box1": search_query1,"search_box2": search_query2})