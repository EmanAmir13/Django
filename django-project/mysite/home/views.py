from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    people_list = [
        {'name': 'Eman', 'age': 21},
        {'name': 'Sana', 'age': 31},
        {'name': 'Aliya', 'age': 17},
        {'name': 'Ali', 'age': 21},
        {'name': 'Mina', 'age': 14}
    ]

    text = '''
    Hello there! Welcome to the world of simplicity. In this space, you can explore the beauty of plain text, free from the distractions of formatting and embellishments. Take a moment to appreciate the elegance of simplicity and let your imagination paint the vivid colors within the canvas of these words. Enjoy the tranquility of pure, unadorned text!
    '''

    return render(request, "home/index.html",
                  context={"page": "My First Project", "people_list": people_list, "text": text})


def about(request):
    context = {"page": "About"}
    return render(request, "home/about.html", context)


def contact(request):
    context = {"page": "Contact"}
    return render(request, "home/contact.html", context)
