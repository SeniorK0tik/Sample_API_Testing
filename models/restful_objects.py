import datetime
from typing import TypedDict, Dict

from pydantic import RootModel, Field, NonNegativeInt, NonNegativeFloat, BaseModel, field_validator

from utils.fakers import random_string, random_int_number, random_float_number


class MyBaseModel(BaseModel):
    class Config:
        extra = 'forbid'


class DefaultData(MyBaseModel):
    year: NonNegativeInt | None = Field(
        default_factory=random_int_number)
    price: NonNegativeFloat | None = Field(
        default_factory=random_float_number)
    cpu_model: str | None = Field(
        default_factory=random_string,
        alias="CPU model"
    )
    color: str | None = Field(default_factory=random_string)
    capacity: str | None = Field(default_factory=random_string)
    capacity_gb: NonNegativeInt | None = Field(
        default_factory=random_int_number,
        alias="capacity GB"
    )
    generation:  str | None = Field(default_factory=random_string)
    hard_disk_size: str | None = Field(
        default_factory=random_string,
        alias="Hard disk size"
    )
    strap_color: str | None = Field(
        default_factory=random_string,
        alias="Strap Colour"
    )
    case_size: str | None = Field(
        default_factory=random_string,
        alias="Case Size"
    )
    u_color: str | None = Field(
        default_factory=random_string,
        alias="Color"
    )
    description: str | None = Field(
        default_factory=random_string,
        alias="Description"
    )
    u_capacity: str | None = Field(
        default_factory=random_string,
        alias="Capacity"
    )
    screen_size: NonNegativeFloat | None = Field(
        default_factory=random_float_number,
        alias="Screen size"
    )
    u_generation: str | None = Field(
        default_factory=random_string,
        alias="Generation"
    )
    u_price: str | None = Field(
        default_factory=random_string,
        alias="Price"
    )


class DefaultRestfulObject(MyBaseModel):
    id: str | None = Field(default_factory=random_string)
    name: str | None = Field(default_factory=random_string)
    data: DefaultData | None = Field(default=None)


class NewRestfulObject(DefaultRestfulObject):
    """Post Request Model"""
    created_at: str = Field(alias="createdAt")

    @field_validator('created_at')
    def validate_created_at(cls, v):
        assert datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f%z')


class DefaultRestfulObjects(RootModel):
    root: list[DefaultRestfulObject]


class UpdateDefaultRestfulObject(BaseModel):
    """Before update"""
    name: str = Field(default_factory=random_string)
    data: DefaultData | None = Field(default=None)


class UpdatedDefaultRestfulObject(UpdateDefaultRestfulObject):
    """After Update"""
    update_at: str = Field(alias="updatedAt")


class PatchedDefaultRestfulObject(BaseModel):
    name: str = Field(default_factory=random_string)
    data: DefaultData | None = Field(default=None)


class RestfulObjectDict(TypedDict):
    id: int
    name: str
    data: Dict[str, str | int | float]


class NewRestfulObjectDict(RestfulObjectDict):
    createdAt: str


class UpdatedRestfulObjectDict(RestfulObjectDict):
    updatedAt: str
