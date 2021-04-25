from fastapi import APIRouter

from resources import web


api_router = APIRouter()


api_router.include_router(web.router, prefix='', tags=['Ресурсы'])
