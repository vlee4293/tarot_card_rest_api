from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session

fortune_router = APIRouter(prefix="/fortunes")


@fortune_router.get("", response_model=List[schemas.FortuneDetail])
def list_fortunes(tarot_id: int, session=Depends(get_session)):
    stmt = (
        select(models.FortuneModel)
        .join(models.FortuneModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    results = session.execute(stmt).scalars().all()

    return results
