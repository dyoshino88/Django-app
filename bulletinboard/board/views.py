from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Topics, Texts
from django.http import Http404
from django.core.cache import cache
from django.http import JsonResponse
from django.http import HttpRequest

def create_topic(request):
  create_topic_form = forms.CreateTopicForm(request.POST or None)
  if create_topic_form.is_valid():
    create_topic_form.instance.user = request.user
    create_topic_form.save()
    messages.success(request, '掲示板が作成されました')
    return redirect('board:list_topics')
  return render(
    request, 'board/create_topic.html', context={
      'create_topic_form': create_topic_form,
    }
  )

def list_topics(request): 
  topics = Topics.objects.pick_all_topics()
  return render(
    request, 'board/list_topics.html', context={
      'topics': topics
    }
  )
  
def edit_topic(request, id): 
  topic = get_object_or_404(Topics, id=id)
  if topic.user.id != request.user.id:
    raise Http404
  edit_topic_form = forms.CreateTopicForm(request.POST or None, instance=topic)
  if edit_topic_form.is_valid():
    # セッションデータの取得
    session_data = request.session.get('add_session')
    # セッションの有無を確認
    if 'add_session' in request.session:
      print('セッション名add_sessionは存在します')
    else :
      print('セッション名add_sessionは存在しません')
    edit_topic_form.save()
    messages.success(request, '掲示板が更新されました')
    return redirect('board:list_topics')
  return render(
    request, 'board/edit_topic.html', context={
      'edit_topic_form': edit_topic_form,
      'id': id,
    }
  )
  
def delete_topic(request, id): 
  topic = get_object_or_404(Topics, id=id)
  if topic.user.id != request.user.id:
    raise Http404
  delete_topic_form = forms.DeleteTopicForm(request.POST or None)
  if delete_topic_form.is_valid():
    topic.delete()
    messages.success(request, '掲示板が削除されました')
    return redirect('board:list_topics')
  return render(
    request, 'board/delete_topic.html', context={
      'delete_topic_form': delete_topic_form
    }
  )

def post_texts(request, topic_id):
  saved_text = cache.get(f'saved_text-topic_id={topic_id}-user_id={request.user.id}', '')
  post_text_form = forms.PostTextForm(request.POST or None, initial={'text':saved_text})
  topic = get_object_or_404(Topics, id=topic_id)
  texts = Texts.objects.pick_by_topic_id(topic_id)
  if post_text_form.is_valid():
    if not request.user.is_authenticated:
      raise Http404
    post_text_form.instance.topic = topic
    post_text_form.instance.user = request.user
    post_text_form.save()
    cache.delete(f'saved_text-topic_id={topic_id}-user_id={request.user.id}')
    return redirect('board:post_texts', topic_id=topic_id)
  return render(
    request, 'board/post_texts.html', context={
      'post_text_form': post_text_form,
      'topic': topic,
      'texts': texts,
    }
  )

def save_text(request: HttpRequest):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        text = request.GET.get('text')
        topic_id = request.GET.get('topic_id')
        if text and topic_id:
            cache.set(f'saved_text-topic_id={topic_id}-user_id={request.user.id}', text)
            return JsonResponse({'message': '投稿が一時保存されました'})
    return JsonResponse({}, status=400)


  
# Create your views here.
