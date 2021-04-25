from typing import List

import settings

from fastapi import FastAPI, HTTPException, APIRouter, Depends, BackgroundTasks, Form
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

import random
import string
import datetime
from models import *


router = APIRouter()


@router.get("/", response_model=List[Ticket_Pydantic])
async def get_tickets():
    return await Ticket_Pydantic.from_queryset(Tickets.all())


@router.get("/{ticket_id}", response_model=Ticket_Pydantic)
async def get_ticket(ticket_id: int):
    return await Ticket_Pydantic.from_queryset_single(Tickets.get(id=ticket_id))


@router.post("/", response_model=Ticket_Pydantic)
async def create_ticket(name: str = Form(...), phone: str = Form(...), problem: str = Form(...)):
    ticket = {
        'name': name,
        'phone': phone,
        'problem': problem
        }
    ticket_obj = await Tickets.create(**ticket)
    return await Ticket_Pydantic.from_tortoise_orm(ticket_obj)


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int):
    await Tickets.filter(id=ticket_id).delete()
    return {'status': 'ok'}
