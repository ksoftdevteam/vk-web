import settings

import uvicorn
from uvicorn import Config, Server

import logging

import asyncio

from fastapi import FastAPI
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

import ticket
import resources

import pickle
import os

app = FastAPI(
    title="Ням-Ням API",
    docs_url=f'{settings.API_V1_STR}/documentation',
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(ticket.api_router, prefix='/ticket')
app.include_router(resources.api_router, prefix='/resources')


register_tortoise(
    app,
    db_url=f'postgres://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_CONTAINER_NAME}:5432/{settings.POSTGRES_DB}',
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    config = Config(app=app, host=settings.WEBAPP_HOST, port=settings.WEBAPP_PORT, loop=loop)
    server = Server(config)
    loop.create_task(server.serve())


    loop.run_forever()
