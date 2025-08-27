from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session

keyword_router = APIRouter(prefix="/keywords")


@keyword_router.get("", response_model=List[schemas.KeywordDetail])
def list_keywords(tarot_id: int, session=Depends(get_session)):
    stmt = (
        select(models.KeywordModel)
        .join(models.KeywordModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    results = session.execute(stmt).scalars().all()

    return results
