from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select

from tarot_cards_rest import models, schemas
from tarot_cards_rest.database import get_session

meanings_router = APIRouter(prefix="/meanings")


@meanings_router.get("", response_model=schemas.MeaningCollection)
def list_meanings(tarot_id: int, session=Depends(get_session)):
    stmt = (
        select(models.MeaningLightModel)
        .join(models.MeaningLightModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    light = session.execute(stmt).scalars().all()
    stmt = (
        select(models.MeaningShadowModel)
        .join(models.MeaningShadowModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    shadow = session.execute(stmt).scalars().all()

    return {"light": light, "shadow": shadow}


@meanings_router.get("/light", response_model=List[schemas.MeaningDetail])
def list_meanings_light(tarot_id: int, session=Depends(get_session)):
    stmt = (
        select(models.MeaningLightModel)
        .join(models.MeaningLightModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    results = session.execute(stmt).scalars().all()

    return results


@meanings_router.get("/shadow", response_model=List[schemas.MeaningDetail])
def list_meanings_shadow(tarot_id: int, session=Depends(get_session)):
    stmt = (
        select(models.MeaningShadowModel)
        .join(models.MeaningShadowModel.tarots)
        .where(models.TarotModel.id == tarot_id)
    )
    results = session.execute(stmt).scalars().all()

    return results
