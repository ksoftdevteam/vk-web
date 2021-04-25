from fastapi import APIRouter

from ticket import (
    web, api
    )


api_router = APIRouter()


api_router.include_router(web.router, prefix='', tags=['Служба поддержки WEB'])
api_router.include_router(api.router, prefix='/api', tags=['Служба поддержки API'])
