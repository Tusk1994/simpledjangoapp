from django.db import models


class Clients(models.Model):
    first_name = models.CharField('First_name', max_length=50)
    last_name = models.CharField('Last_name', max_length=100)
    country = models.CharField('Country', max_length=100)

    def __repr__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        db_table = 'clients'
        verbose_name_plural = "Clients"


class Payments(models.Model):
    payer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    amount = models.FloatField('Amount')
    percent = models.IntegerField('Percent')
    pay_date = models.DateTimeField('Date payment')

    def __repr__(self):
        return '{0}: {1}'.format(self.payer, self.amount)

    class Meta:
        db_table = 'payments'
        verbose_name_plural = "Payments"
