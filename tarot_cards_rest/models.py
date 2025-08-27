from typing import List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    declared_attr,
)

from tarot_cards_rest.utils import snake_slugify


__all__ = [
    "ArcanaModel",
    "SuitModel",
    "FortuneModel",
    "KeywordModel",
    "MeaningLightModel",
    "MeaningShadowModel",
    "ArchetypeModel",
    "HebrewAlphabetModel",
    "NumerologyModel",
    "ElementalModel",
    "MythicalSpiritualModel",
    "AstrologyModel",
    "AffirmationModel",
    "TarotModel",
]


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return snake_slugify(cls.__name__.removesuffix("Model"))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class ArcanaModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="arcana",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class SuitModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="suit",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


_tarot_fortune_link = Table(
    "tarot_fortune_link",
    Base.metadata,
    Column("tarot_id", ForeignKey("tarot.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "fortune_id", ForeignKey("fortune.id", ondelete="CASCADE"), primary_key=True
    ),
)


class FortuneModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        secondary=_tarot_fortune_link,
        back_populates="fortunes",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


_tarot_keyword_link = Table(
    "tarot_keyword_link",
    Base.metadata,
    Column("tarot_id", ForeignKey("tarot.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "keyword_id", ForeignKey("keyword.id", ondelete="CASCADE"), primary_key=True
    ),
)


class KeywordModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        secondary=_tarot_keyword_link,
        back_populates="keywords",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


_tarot_meaning_light_link = Table(
    "tarot_meaning_light_link",
    Base.metadata,
    Column("tarot_id", ForeignKey("tarot.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "meaning_light_id",
        ForeignKey("meaning_light.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class MeaningLightModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        secondary=_tarot_meaning_light_link,
        back_populates="meanings_light",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


_tarot_meaning_shadow_link = Table(
    "tarot_meaning_shadow_link",
    Base.metadata,
    Column("tarot_id", ForeignKey("tarot.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "meaning_shadow_id",
        ForeignKey("meaning_shadow.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class MeaningShadowModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        secondary=_tarot_meaning_shadow_link,
        back_populates="meanings_shadow",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class ArchetypeModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="archetype",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class HebrewAlphabetModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="hebrew_alphabet",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class NumerologyModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="numerology",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class ElementalModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="elemental",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class MythicalSpiritualModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="mythical_spiritual",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class AstrologyModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="astrology",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class AffirmationModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)

    tarots: Mapped[List["TarotModel"]] = relationship(
        back_populates="affirmation",
        cascade="all, delete",
        passive_deletes=True,
        order_by="TarotModel.id",
    )


class TarotModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    number_repr: Mapped[int]
    img_file: Mapped[str] = mapped_column(unique=True)
    arcana_id: Mapped[int] = mapped_column(ForeignKey("arcana.id", ondelete="CASCADE"))
    suit_id: Mapped[int] = mapped_column(ForeignKey("suit.id", ondelete="CASCADE"))
    archetype_id: Mapped[int] = mapped_column(
        ForeignKey("archetype.id", ondelete="CASCADE"), nullable=True
    )
    hebrew_alphabet_id: Mapped[int] = mapped_column(
        ForeignKey("hebrew_alphabet.id", ondelete="CASCADE"), nullable=True
    )
    numerology_id: Mapped[int] = mapped_column(
        ForeignKey("numerology.id", ondelete="CASCADE"), nullable=True
    )
    elemental_id: Mapped[int] = mapped_column(
        ForeignKey("elemental.id", ondelete="CASCADE"), nullable=True
    )
    mythical_spiritual_id: Mapped[int] = mapped_column(
        ForeignKey("mythical_spiritual.id", ondelete="CASCADE"), nullable=True
    )
    astrology_id: Mapped[int] = mapped_column(
        ForeignKey("astrology.id", ondelete="CASCADE"), nullable=True
    )
    affirmation_id: Mapped[int] = mapped_column(
        ForeignKey("affirmation.id", ondelete="CASCADE"), nullable=True
    )

    arcana: Mapped["ArcanaModel"] = relationship(back_populates="tarots")
    suit: Mapped["SuitModel"] = relationship(back_populates="tarots")
    fortunes: Mapped[List["FortuneModel"]] = relationship(
        secondary=_tarot_fortune_link, back_populates="tarots"
    )
    keywords: Mapped[List["KeywordModel"]] = relationship(
        secondary=_tarot_keyword_link, back_populates="tarots"
    )
    meanings_light: Mapped[List["MeaningLightModel"]] = relationship(
        secondary=_tarot_meaning_light_link, back_populates="tarots"
    )
    meanings_shadow: Mapped[List["MeaningShadowModel"]] = relationship(
        secondary=_tarot_meaning_shadow_link, back_populates="tarots"
    )
    archetype: Mapped["ArchetypeModel"] = relationship(back_populates="tarots")
    hebrew_alphabet: Mapped["HebrewAlphabetModel"] = relationship(
        back_populates="tarots"
    )
    numerology: Mapped["NumerologyModel"] = relationship(back_populates="tarots")
    elemental: Mapped["ElementalModel"] = relationship(back_populates="tarots")
    mythical_spiritual: Mapped["MythicalSpiritualModel"] = relationship(
        back_populates="tarots"
    )
    astrology: Mapped["AstrologyModel"] = relationship(back_populates="tarots")
    affirmation: Mapped["AffirmationModel"] = relationship(back_populates="tarots")
