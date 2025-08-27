from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session


arcana_router = APIRouter(prefix="/arcanas", tags=["arcana"])


@arcana_router.get("", response_model=List[schemas.ArcanaDetail])
def list_arcanas(session=Depends(get_session)):
    stmt = select(models.ArcanaModel).options(joinedload(models.ArcanaModel.tarots))
    results = session.execute(stmt).scalars().unique().all()

    return results


@arcana_router.get("/{arcana_id}", response_model=schemas.ArcanaDetail)
def get_arcana(arcana_id: int, session=Depends(get_session)):
    stmt = (
        select(models.ArcanaModel)
        .options(joinedload(models.ArcanaModel.tarots))
        .where(models.ArcanaModel.id == arcana_id)
    )
    results = session.execute(stmt).scalars().unique().one_or_none()
    if results:
        return results

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
