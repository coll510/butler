from django.contrib import admin
from .models import Book, Event, Member, Order, Event_Attendance, Forum, Topic, Reply
import decimal
from django.db.models import F



# Register your models here.


"""
register class model in django admin and customize it
"""

def apply_discount(modeladmin, request, queryset):
    queryset.update(price=F('price') * decimal.Decimal('0.9'))
    apply_discount.short_description = 'Apply 10%% discount'

def change_price(modeladmin, request, queryset):
    for book in queryset:
        book.price = 19.99
        book.save()
change_price.short_description = 'Change price'

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    list_filter = ("series",)
    actions = [apply_discount, change_price]

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("book_id", "facilitator")

class TopicAdmin(admin.ModelAdmin):
    list_display = ("forum", "title", "member_id", "date_created")
    list_filter = ("forum", "member_id")

class ReplyAdmin(admin.ModelAdmin):
    # list_display = ("topic", "date_created")
    list_filter = ("member_id",)

class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email")
    list_filter = ("username", "email")
    search_fields = ("last_name__startswith", "first_name__startswith")

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
