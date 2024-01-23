from django.db import models


class Ticket(models.Model):
    # id: int = models.IntegerField(primary_key=True, )
    title: str = models.CharField(max_length=100)
    details: str = models.TextField(default="")
    priority: str = models.CharField(max_length=3, default="")
    state: int = models.IntegerField(default=0)
    necessary_tickets = models.ManyToManyField("self", default=None, blank=True)

    class Meta:
        ordering = ["id"]


class NecessaryTickets(models.Model):
    id_master_ticket: int = models.ForeignKey(
        to=Ticket,
        related_name="id_master_ticket",
        on_delete=models.CASCADE,
    )
    id_slave_ticket: int = models.ForeignKey(
        to=Ticket,
        related_name="id_slave_ticket",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (("id_master_ticket", "id_slave_ticket"),)
