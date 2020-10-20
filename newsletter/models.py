from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=300, help_text='Email klienta')
    name = models.CharField(max_length=400, help_text='Imie klienta')
    permission = models.BooleanField(help_text='Zgoda na marketing klienta')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.name + " - " + self.email + "; zapisany: " + self.update_date.__str__()
