from fastapi import FastAPI

from tarot_cards_rest.tarots.router import tarots_router
from tarot_cards_rest.arcanas.router import arcana_router
from tarot_cards_rest.suits.router import suit_router

api = FastAPI()
api.include_router(tarots_router)
api.include_router(arcana_router)
api.include_router(suit_router)
