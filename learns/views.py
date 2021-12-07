import os
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
from django.shortcuts import render

from config import settings
from learns.forms import PostForm
from learns.models import Post

def download_file(request, file_name):
    file_path = os.path.join(settings.PRIVATE_STORAGE_ROOT, file_name)
    filename = os.path.basename(file_path)
    chunk_size = 8192
    response = StreamingHttpResponse(
        FileWrapper(open(file_path, 'rb'), chunk_size),
        content_type="application/octet-stream"
    )
    response['Content-Length'] = os.path.getsize(file_path)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



def post_list(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        form = PostForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['author']:
                posts = posts.filter(author__home_page=form.cleaned_data['author'])
    else:
        form = PostForm()


    context = {'posts': posts, 'form': form}
    return render(request, 'learns/post.html', context)