from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import EmailForm
from .models import HomePage
from .models import Article, Service

# Create your views here.


def index(request):
    content = HomePage.objects.first()
    context = {
        'content': content
    }
    return render(request, 'website/index.html', context) 


def contact_view(request):
    return render(request, 'website/contact.html')


@csrf_exempt
def contact_async(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #send email
            subject = 'Contact Form Submission'
            message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            from_email = email  # sent from email user inputted into form
            recipient_list = ['ray1k190s@gmail.com']

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)






# def contact_view(request):
#     # form = EmailForm()
#     # success = False

#     # if request.method == 'POST':
#     #     form = EmailForm(request.POST)
#     #     if form.is_valid():
#     #         # Process the form data, e.g., send an email.
#     #         subject = 'Contact Form Submission'
#     #         message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nMessage:\n{form.cleaned_data["message"]}'
#     #         from_email = request.POST["email"]
#     #         # sender = request.POST["name"]
#     #         recipient_list = ['ray1992k@gmail.com']

#     #         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     #         success = True
#     #         return redirect('success')

#             # Set success to True to indicate a successful form submission
#     return render(request, 'website/contact.html')   # {'form': form, 'success': success}





def success(request):
    return render(request, 'website/form_success.html') 

def career(request):
    return render(request, 'website/career_guidance.html')

def vocation(request):
    return render(request, 'website/vocation_blog.html')

def training(request):
    return render(request, 'website/training.html')

def articles(request):
    articles = Article.objects.all() #you need to add in order  by but first need to add date in model

    context = {
        "articles" : articles
    }

    return render(request, 'website/articles.html', context)



def article_post(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "article" : article
    }

    return render(request, 'website/article_post.html', context)

def service_page(request, slug):
    service = get_object_or_404(Service, slug=slug)

    context = {
        "service" : service,
    }

    return render(request, 'website/service_page.html', context)

