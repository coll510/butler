from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    series = models.CharField(max_length=50, blank=True)
    published = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Event(models.Model):

    book_id = models.ForeignKey(Book, on_delete=models.PROTECT, related_name ="events")
    date = models.DateField()
    facilitator = models.CharField(max_length=50)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Member(models.Model):

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=24)

    def __str__(self):
        return self.username


class Order(models.Model):

    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    member_id = models.ForeignKey(Member, on_delete=models.PROTECT)
    total = models.FloatField()
    date = models.DateField()

class Event_Attendance(models.Model):

    event_id = models.ForeignKey(Event, on_delete=models.PROTECT)
    member_id = models.ForeignKey(Member, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.event_id)

class Forum(models.Model):

    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Topic(models.Model):

    forum = models.ForeignKey(Forum, on_delete=models.PROTECT, related_name="topics")
    member_id = models.ForeignKey(Member, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
  
    def __str__(self):
        return self.title

class Reply(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="replies")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    comment = models.TextField()
    
    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('edit_reply', kwargs={'pk': self.pk})





   