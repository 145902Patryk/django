from django.db import models
from crum import get_current_user
from datetime import datetime


class Uczestnicy(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    email = models.CharField(max_length=40, default='')
    telefon = models.CharField(max_length=9)

    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.nazwisko, self.imie)


class Organizatorzy(models.Model):
    nazwa = models.CharField(max_length=30)
    email = models.CharField(max_length=40, default='')
    telefon = models.CharField(max_length=9)
    stworzony_przez = models.ForeignKey('auth.User', blank=True, default=get_current_user(),
                                        on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)

    objects = models.Manager()

    def __str__(self):
        return self.nazwa

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Organizatorzy, self).save(*args, **kwargs)


class Szkolenia(models.Model):
    nazwa = models.CharField(max_length=30)
    data = models.DateField()
    adres = models.CharField(max_length=70)
    cena = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    opic = models.TextField(blank=True)
    idOrganizatora = models.ForeignKey(Organizatorzy, on_delete=models.CASCADE)

    object = models.Manager()

    def __str__(self):
        return '%s %s' % (self.nazwa, self.idOrganizatora)


class UczestnicySzkolen(models.Model):
    idSzkolenia = models.ForeignKey(Szkolenia, on_delete=models.CASCADE)
    idUczestnika = models.ForeignKey(Uczestnicy, on_delete=models.CASCADE)

    object = models.Manager()

    def __str__(self):
        return '%s %s' % (self.idSzkolenia, self.idUczestnika)
