from pydantic import Field

from settings import base_settings
from utils.models.base_model import BaseModel


class AuthUser(BaseModel):
    email: str | None = Field(default=None)
    password: str | None = Field(default=None)


class Authentication(BaseModel):
    auth_token: str | None = Field(default=base_settings.api_key)
    user: AuthUser | None = AuthUser()
