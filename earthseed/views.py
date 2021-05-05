from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormMixin, UpdateView, DeleteView
from django.views import generic
from django.http import JsonResponse

from .models import *
from .forms import TopicForm, ReplyForm, EventAttendanceForm, OrderBookForm
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.


class BookList(ListView):
    model = Book

class EventList(ListView):
    model = Event

class ForumList(generic.ListView, FormMixin):
    model = Forum
    template_name = 'forum_list.html'
    context_object_name = 'forums'
    form_class = TopicForm


def post_topic(request):
    context ={}
  
    # create object of form
    form = TopicForm(request.POST or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('/')
  
    context['form']= form
    return render(request, "earthseed/post_topic.html", context)


def post_reply(request):
    context ={}
  
    # create object of form
    form = ReplyForm(request.POST or None)
      
    if form.is_valid():
        form.save()
        return redirect('/')
  
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

    form = OrderBookForm(request.POST or None)
    # book = Book.objects.all()

    if form.is_valid():
        form.save()
        return redirect('/')

    # context = {'form': form, 
    #             'book': book}
    context['form']= form
    return render(request, "earthseed/order_book.html", context)

class TopicUpdate(UpdateView):
    model = Topic
    fields = ['title', 'content']
    success_url = reverse_lazy('forum_list')

class ReplyUpdate(UpdateView):
    model = Reply
    fields = ['comment']
    success_url = reverse_lazy('forum_list')
    template_name_suffix = '_form'

class ReplyDelete(DeleteView):
    model = Reply
    success_url = reverse_lazy('forum_list')


# from bootstrap_modal_forms.generic import BSModalCreateView
# class TopicCreateView(BSModalCreateView):
#     template_name = 'earthseed/post_topic.html'
#     form_class = TopicForm
#     success_message = 'Success: Topic was posted.'
#     success_url = reverse_lazy('forum_list')

# def topics(request):
#     form = TopicForm()
#     if request.is_ajax and request.method == "POST":
#         # get the form data
#         form = TopicForm(request.POST)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             instance = form.save()
#             # serialize in new topic object in json
#             ser_instance = serializers.serialize('json', [ instance, ])
#             # send to client side.
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             # some form errors occured.
#             return JsonResponse({"error": form.errors}, status=400)

#     return render(request, "earthseed/post_topic.html", {'form': form})
    # some error occured
    # return JsonResponse({"error": ""}, status=400)