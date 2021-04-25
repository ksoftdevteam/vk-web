from typing import List

import settings

from fastapi import FastAPI, HTTPException, APIRouter, Depends, BackgroundTasks
from fastapi.responses import FileResponse

from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

import random
import string
import datetime
from models import *


router = APIRouter()


@router.get("/{resource_name}")
async def get_resource(resource_name: str):
    return FileResponse('/backend/app/templates/' + resource_name)
