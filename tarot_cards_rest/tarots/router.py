from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy import select

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session
from tarot_cards_rest.tarots.fortunes.router import fortune_router
from tarot_cards_rest.tarots.keywords.router import keyword_router
from tarot_cards_rest.tarots.meanings.router import meanings_router


tarots_router = APIRouter(prefix="/tarots", tags=["tarot"])


@tarots_router.get(
    "", response_model=List[schemas.TarotDetail], response_model_exclude_none=True
)
def list_tarots(session=Depends(get_session)):
    stmt = select(models.TarotModel)
    results = session.execute(stmt).scalars().all()

    return results


@tarots_router.get(
    "/{tarot_id}", response_model=schemas.TarotDetail, response_model_exclude_none=True
)
def get_tarot(tarot_id: int, session=Depends(get_session)):
    stmt = select(models.TarotModel).where(models.TarotModel.id == tarot_id)
    results = session.execute(stmt).scalars().one_or_none()
    if results:
        return results

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


tarots_router.include_router(fortune_router, prefix="/{tarot_id}")
tarots_router.include_router(keyword_router, prefix="/{tarot_id}")
tarots_router.include_router(meanings_router, prefix="/{tarot_id}")
