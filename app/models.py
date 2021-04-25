from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Tickets(models.Model):
    """
    Модель тикета
    """

    id = fields.IntField(pk=True)
    #: ФИО
    name = fields.TextField()
    #: Номер телефона
    phone = fields.TextField()
    #: Текст проблемы
    problem = fields.TextField()

Ticket_Pydantic = pydantic_model_creator(Tickets, name="Ticket")
TicketIn_Pydantic = pydantic_model_creator(Tickets, name="TicketIn", exclude_readonly=True)