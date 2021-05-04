from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import generic
from django.http import JsonResponse

from .models import *
from .forms import TopicForm, ReplyForm, EventAttendanceForm, OrderBook
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.


class BookList(ListView):
    model = Book

class EventList(ListView):
    model = Event

class ForumList(generic.ListView):
    model = Forum
    template_name = 'forum_list.html'
    context_object_name = 'forums'
    
# class TopicList(ListView):
#     model = Topic
#     template_name = 'topic_list.html'


# def home(request):
#     forums=forum.objects.all()
#     count=forums.count()
#     discussions=[]
#     for i in forums:
#         discussions.append(i.discussion_set.all())
 
#     context={'forums':forums,
#               'count':count,
#               'discussions':discussions}
#     return render(request,'home.html',context)

# def forum_filter(request):
#     f = ForumFilter(request.GET, queryset= Forum.objects.all())
#     return render(request, 'earthseed/topic_list.html', {'filter': f})

# def show_topics(request):
#     # forums = Forum.objects.all()
#     topics = Topic.objects.order_by('forum')
#     replies = []

#     for topic in topics:
#         replies.append(topic.reply_set.all())

#     context = {'topics': topics, 
#                 'replies': replies}

#     return render(request, 'earthseed/topic_list.html', context)

#     forum = Forum.objects.all()
#     forum_data = {}
#     forum_data['object_list'] = forum

#     return render(request, "earthseed/topic_list.html", forum_data)

# def addInForum(request):
#     form = CreateInForum()
#     if request.method == 'POST':
#         form = CreateInForum(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context ={'form':form}
#     return render(request,'addInForum.html',context)
 
# def addInDiscussion(request):
#     form = CreateInDiscussion()
#     if request.method == 'POST':
#         form = CreateInDiscussion(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context ={'form':form}
#     return render(request,'addInDiscussion.html',context)

# class ReplyList(ListView):
#     model = Reply
#     template_name = 'topics_list.html'



# function to show forums instead of using CBV
# def list_forums(request):

#     forum = Forum.objects.all()
#     topic = Topic.objects.filter(forum_id__id = 1)
#     reply = Reply.objects.all()
#     context = {'forum': forum, 'topic': topic, 'reply': reply}
#     return render(request, "earthseed/forum_list.html", context=context)


    # forum = Forum.objects.all()
    # topic = Topic.objects.all()
    # reply = Reply.objects.all()
    # topic = []
    # reply = []


    # for item in forum:
    #     # topic_query = Topic.objects.filter(Topic.forum_id == item.id)
    #     # if topic_query:
    #     #     topic.append(topic_query)
    #         reply_query = Reply.objects.filter(Reply.topic_id == Topic.id)
    #         if reply_query:
    #             reply.append(reply_query)

    # context = {'forum': forum, 'topic': topic, 'reply': reply}
    # return render(request, "earthseed/forum_list.html", context=context)
    # ---------------------------------------


    # forum = Forum.objects.all()

    # forum_data = {}
    # forum_data['object_list'] = forum
    # topic = Topic.objects.all()
    # topics = []

    # for i in forum:
    #     topics.append(topic)

    # context = {'forum': forum, 
    #             'topic': topic}

    # forum = Forum.objects.all()
    # topic = Topic.objects.all()
    # reply = Reply.objects.all()
    # forum_data = {}
    # topic_data = {}
    # reply_data = {}
    # forum_data['object_list'] = forum
    # topic_data['object_list'] = topic 
    # reply_data['object_list'] = reply

    # payload = {'forum': forum_data, 
    #           'topic': topic_data} 
    #             # 'reply': reply}
    
    # forums_dict = {
    #     "template_name": "earthseed/forum_list.html",
    #     "queryset": Forum.objects.all(),
    #     "extra_context" : {"topic_list" : Topic.objects.all(),
    #                        "reply_list": Reply.objects.all()}
    # }

    # queryset = {
    #             "forum_list": Forum.objects.all(),
    #             "topic_list" : Topic.objects.all(),
    #             "reply_list": Reply.objects.all()
    # }

    
    # return render(request, "earthseed/forum_list.html", queryset)
    # return forums_dict

# view renders TopicForm and saves to DB


class TopicCreateView(BSModalCreateView):
    template_name = 'earthseed/post_topic.html'
    form_class = TopicForm
    success_message = 'Success: Topic was posted.'
    success_url = reverse_lazy('forum_list')

def topics(request):
    form = TopicForm()
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = TopicForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new topic object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    return render(request, "earthseed/post_topic.html", {'form': form})
    # some error occured
    # return JsonResponse({"error": ""}, status=400)


# commenting this functioning function out to try it with ajax instead directly above
# def post_topic(request):
#     context ={}
  
#     # create object of form
#     form = TopicForm(request.POST or None)
      
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
#         return redirect('forums/')
  
#     context['form']= form
#     return render(request, "earthseed/post_topic.html", context)


def post_reply(request):
    context ={}
  
    # create object of form
    form = ReplyForm(request.POST or None)
      
    if form.is_valid():
        form.save()
        # return redirect('/')
        #http referer keeps member on same page after submitting
        return redirect(request.META.get("HTTP_REFERER", "/"))
  
    context['form']= form
    return render(request, "earthseed/post_reply.html", context)


def event_signup(request):
    context ={}

    form = EventAttendanceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form']= form
    return render(request, "earthseed/event_signup.html", context)

def order_book(request):
    context ={}

    form = OrderBook(request.POST or None)
    # book = Book.objects.all()

    if form.is_valid():
        form.save()
        return redirect('/')

    # context = {'form': form, 
    #             'book': book}
    context['form']= form
    return render(request, "earthseed/order_book.html", context)

