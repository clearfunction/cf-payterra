from pydantic import BaseModel


class VersionResponse(BaseModel):
    version: str = "v0.1.0"
