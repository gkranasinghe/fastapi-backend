from typing import Optional
from enum import Enum

from app.models.core import IDModelMixin, CoreModel


class CleaningType(str, Enum):
    dust_up = "dust_up"
    spot_clean = "spot_clean"
    full_clean = "full_clean"


class CleaningBase(CoreModel):
    """
    All common characteristics of our Cleaning resource
    """
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    cleaning_type: Optional[CleaningType] = "spot_clean"


class CleaningCreate(CleaningBase):
    """attributes required to create a new Cleaning - used at POST requests

    Args:
        CleaningBase (CleaningType): create a new Cleaning used at POST requests
    """
    name: str
    price: float


class CleaningUpdate(CleaningBase):
    """
    attributes required to update a Cleaning - used at POST requests"""
    cleaning_type: Optional[CleaningType]


class CleaningInDB(IDModelMixin, CleaningBase):
    """
    Attributes  present on any resource coming out of the database
        cleaning_type (CleaningType):"""
    name: str
    price: float
    cleaning_type: CleaningType


class CleaningPublic(IDModelMixin, CleaningBase):
    """
    attributes present on public facing resources being returned from GET, POST, and PUT requests
    """
    pass

