from pydantic import BaseModel


class DefaultResponse(BaseModel):
    message: str = "Welcome to Clear Function's Payterra API! Navigate to `/docs` for Swagger Specification."
