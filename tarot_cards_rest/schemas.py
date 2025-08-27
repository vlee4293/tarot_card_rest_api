from typing import List, Optional
from pydantic import BaseModel, ConfigDict

__all__ = [
    "ArcanaSummary",
    "ArcanaDetail",
    "SuitSummary",
    "SuitDetail",
    "FortuneDetail",
    "FortuneDetail",
    "KeywordDetail",
    "KeywordDetail",
    "MeaningDetail",
    "ArchetypeSummary",
    "ArchetypeDetail",
    "HebrewSummary",
    "HebrewDetail",
    "NumerologySummary",
    "NumerologyDetail",
    "ElementalSummary",
    "ElementalDetail",
    "MythicalSummary",
    "MythicalDetail",
    "AstrologySummary",
    "AstrologyDetail",
    "AffirmationSummary",
    "AffirmationDetail",
    "TarotSummary",
    "TarotDetail",
]


class ArcanaSummary(BaseModel):
    id: int
    name: str


class ArcanaDetail(ArcanaSummary):
    tarots: List["TarotSummary"]


class SuitSummary(BaseModel):
    id: int
    name: str


class SuitDetail(SuitSummary):
    tarots: List["TarotSummary"]


class FortuneDetail(BaseModel):
    id: int
    description: str


class KeywordDetail(BaseModel):
    id: int
    description: str


class MeaningDetail(BaseModel):
    id: int
    description: str


class MeaningCollection(BaseModel):
    light: List[MeaningDetail]
    shadow: List[MeaningDetail]


class ArchetypeSummary(BaseModel):
    id: int
    name: str


class ArchetypeDetail(ArcanaSummary):
    tarots: List["TarotSummary"]


class HebrewSummary(BaseModel):
    id: int
    description: str


class HebrewDetail(HebrewSummary):
    tarots: List["TarotSummary"]


class NumerologySummary(BaseModel):
    id: int
    description: str


class NumerologyDetail(NumerologySummary):
    tarots: List["TarotSummary"]


class ElementalSummary(BaseModel):
    id: int
    description: str


class ElementalDetail(ElementalSummary):
    tarots: List["TarotSummary"]


class MythicalSummary(BaseModel):
    id: int
    description: str


class MythicalDetail(MythicalSummary):
    tarots: List["TarotSummary"]


class AstrologySummary(BaseModel):
    id: int
    description: str


class AstrologyDetail(AstrologySummary):
    tarots: List["TarotSummary"]


class AffirmationSummary(BaseModel):
    id: int
    description: str


class AffirmationDetail(AffirmationSummary):
    tarots: List["TarotSummary"]


class TarotSummary(BaseModel):
    id: int
    name: str


class TarotDetail(TarotSummary):
    number_repr: int
    img_file: str
    arcana: ArcanaSummary
    suit: SuitSummary
    archetype: Optional[ArchetypeSummary] = None
    hebrew_alphabet: Optional[HebrewSummary] = None
    numerology: Optional[NumerologySummary] = None
    elemental: Optional[ElementalSummary] = None
    mythical_spiritual: Optional[MythicalSummary] = None
    astrology: Optional[AstrologySummary] = None
    affirmation: Optional[AffirmationSummary] = None

    model_config = ConfigDict(from_attributes=True)
