from django import forms
from .models import Topic, Reply, Event_Attendance, Order
from bootstrap_modal_forms.forms import BSModalModelForm

# import django_filters

# class ForumFilter(django_filters.FilterSet):
#     class Meta:
#         model = Forum
#         fields = ['name']

# class TopicForm(forms.ModelForm):


class TopicForm(BSModalModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = "__all__"


class EventAttendanceForm(forms.ModelForm):
    class Meta:
        model = Event_Attendance
        fields = "__all__"


class OrderBook(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["book_id", "member_id"]

  