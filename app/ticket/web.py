from typing import List

import settings

from fastapi import FastAPI, HTTPException, APIRouter, Depends, BackgroundTasks
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

import random
import string
import datetime
from models import *


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def get_ticket_form():
    with open('/backend/app/templates/form.html', 'r') as f:
        html = f.read()
    return html
