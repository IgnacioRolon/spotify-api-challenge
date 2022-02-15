from pydantic import BaseModel, Field


class InputValidation(BaseModel):
    artist: str = Field(description="Artist Name")
