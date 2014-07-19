from django.db import models
from django.forms import ModelForm

class Entry(models.Model):
    ENTRY_TYPE_CHOICES = (
        (-1, 'Expenses'),
        (1, 'Income'),
    )
    desc = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=ENTRY_TYPE_CHOICES)
    category = models.ForeignKey('Categories')

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['desc', 'amount', 'type', 'category']
