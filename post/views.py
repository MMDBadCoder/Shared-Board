from django.conf import settings
from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import MyPost
import validators


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def is_admin(request):
    return get_client_ip(request) in [settings.SERVER_IP, '127.0.0.1']


def posts_page(request):
    data = {
        'title': settings.SERVER_NAME,
        'posts': MyPost.objects.all().order_by('-uploaded_at'),
        'is_admin': is_admin(request),
        'ip': get_client_ip(request),
        'colors': settings.COLORS,
        'names': settings.NAMES
    }
    return render(request, 'posts_page.html', data)


from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def is_link(text):
    return validators.url(text)


def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if form.data['text'] != '' or form.files.__contains__('file'):
                instance = form.save()
                instance.ip = get_client_ip(request)
                instance.save()
    return redirect('posts-page')


def delete_post(request, id):
    MyPost.objects.get(id=id).delete()
    return redirect('posts-page')
