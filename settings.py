import pathlib

from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings

root_dir: pathlib.Path = pathlib.Path(__file__).resolve().parent


class MyBaseSettings(BaseSettings):
    class Config:
        env_file = root_dir.joinpath('.env')
        env_file_encoding = 'utf-8'


class TestUser(BaseModel):
    email: str
    password: str


class Settings(MyBaseSettings):
    base_url: str = Field(..., env='BASE_URL')
    api_key: str = Field(..., env='API_KEY')
    user_email: str | None = Field(default=None)
    user_password: str | None = Field(default=None)

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'

    @property
    def user(self) -> TestUser:
        return TestUser(
            email=self.user_email,
            password=self.user_password
        )


base_settings = Settings()

if __name__ == '__main__':
    print(root_dir)
