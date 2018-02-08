from django.shortcuts import render
import json
from lab1.linkcheck import select_5_from_json
from Django.settings import BASE_DIR


# Create your views here.
def index(request):
    print("base dir path", BASE_DIR)

    return render(request, 'lab1/lab1.html')


def get_more_tables(request):
    increment = int(request.GET['append_increment'])
    increment_int = increment + 1
    data = json.load(open(BASE_DIR + '/lab1/media/TwitterTweets17.json'))
    context = select_5_from_json(increment_int, data)

    return render(request, 'lab1/get_more_tables.html', {"context": context})
