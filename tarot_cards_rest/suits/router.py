from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session


suit_router = APIRouter(prefix="/suits", tags=["suit"])


@suit_router.get("", response_model=List[schemas.SuitDetail])
def list_suits(session=Depends(get_session)):
    stmt = select(models.SuitModel).options(joinedload(models.SuitModel.tarots))
    results = session.execute(stmt).scalars().unique().all()

    return results


@suit_router.get("/{suit_id}", response_model=schemas.SuitDetail)
def get_suit(suit_id: int, session=Depends(get_session)):
    stmt = (
        select(models.SuitModel)
        .options(joinedload(models.SuitModel.tarots))
        .where(models.SuitModel.id == suit_id)
    )
    results = session.execute(stmt).scalars().unique().one_or_none()
    if results:
        return results

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
