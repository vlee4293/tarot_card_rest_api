import json

import pandas as pd
import numpy as np

from sqlalchemy import select

from tarot_cards_rest.database import Session
from tarot_cards_rest.models import (
    ArcanaModel,
    SuitModel,
    TarotModel,
    FortuneModel,
    KeywordModel,
    MeaningLightModel,
    MeaningShadowModel,
    ArchetypeModel,
    HebrewAlphabetModel,
    NumerologyModel,
    ElementalModel,
    MythicalSpiritualModel,
    AstrologyModel,
    AffirmationModel,
)


def get_or_create(session, obj, unique_cols):
    stmt = select(type(obj))
    for col in unique_cols:
        stmt = stmt.where(getattr(type(obj), col) == getattr(obj, col))

    existing = session.execute(stmt).scalar()
    if existing:
        return existing

    session.add(obj)
    session.flush()
    return obj


with open("data/tarot-images.json", "r") as fp:
    data = json.load(fp)

cards = pd.json_normalize(data["cards"])
cards = cards.replace(np.nan, None)


with Session() as session:
    for i, card in cards.iterrows():
        data = ArcanaModel(name=card["arcana"])
        arcana = get_or_create(session, data, ["name"])

        data = SuitModel(name=card["suit"])
        suit = get_or_create(session, data, ["name"])

        optionals = {}
        if card["Archetype"]:
            data = ArchetypeModel(name=card["Archetype"])
            archetype = get_or_create(session, data, ["name"])
            optionals["archetype_id"] = archetype.id

        if card["Hebrew Alphabet"]:
            data = HebrewAlphabetModel(description=card["Hebrew Alphabet"])
            hebrew = get_or_create(session, data, ["description"])
            optionals["hebrew_alphabet_id"] = hebrew.id

        if card["Numerology"]:
            data = NumerologyModel(description=card["Numerology"])
            numerology = get_or_create(session, data, ["description"])
            optionals["numerology_id"] = numerology.id

        if card["Elemental"]:
            data = ElementalModel(description=card["Elemental"])
            elemental = get_or_create(session, data, ["description"])
            optionals["elemental_id"] = elemental.id

        if card["Mythical/Spiritual"]:
            data = MythicalSpiritualModel(description=card["Mythical/Spiritual"])
            myth_spirit = get_or_create(session, data, ["description"])
            optionals["mythical_spiritual_id"] = myth_spirit.id

        if card["Astrology"]:
            data = AstrologyModel(description=card["Astrology"])
            astrology = get_or_create(session, data, ["description"])
            optionals["astrology_id"] = astrology.id

        if card["Affirmation"]:
            data = AffirmationModel(description=card["Affirmation"])
            affirmation = get_or_create(session, data, ["description"])
            optionals["affirmation_id"] = affirmation.id

        session.flush()

        tarot = TarotModel(
            name=card["name"],
            number_repr=card["number"],
            img_file=card["img"],
            arcana_id=arcana.id,
            suit_id=suit.id,
            **optionals,
        )
        tarot = get_or_create(session, tarot, ["name", "img_file"])

        for fortune in card["fortune_telling"]:
            obj = FortuneModel(description=fortune)
            obj = get_or_create(session, obj, ["description"])
            tarot.fortunes.append(obj)

        for keyword in card["keywords"]:
            obj = KeywordModel(description=keyword)
            obj = get_or_create(session, obj, ["description"])
            tarot.keywords.append(obj)

        for meaning in card["meanings.light"]:
            obj = MeaningLightModel(description=meaning)
            obj = get_or_create(session, obj, ["description"])
            tarot.meanings_light.append(obj)

        for meaning in card["meanings.shadow"]:
            obj = MeaningShadowModel(description=meaning)
            obj = get_or_create(session, obj, ["description"])
            tarot.meanings_shadow.append(obj)

        session.commit()
