from django.contrib import admin
from .models import Book, Event, Member, Order, Event_Attendance, Forum, Topic, Reply

# Register your models here.


"""
register class model in django admin and customize it
"""
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    list_filter = ("series",)

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("book_id",)

class TopicAdmin(admin.ModelAdmin):
    list_display = ("forum", "title", "member_id", "date_created")
    list_filter = ("forum", "member_id")

class ReplyAdmin(admin.ModelAdmin):
    # list_display = ("topic", "date_created")
    list_filter = ("member_id",)

class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email")
    list_filter = ("username", "email")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("book_id", "date")
    list_filter = ("book_id", "date")

admin.site.register(Book, BookAdmin)
# admin.site.register(Book)
admin.site.register(Event, EventAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Event_Attendance)
admin.site.register(Forum)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
