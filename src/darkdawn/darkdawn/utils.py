from pydantic import BaseModel


class MappedURL(BaseModel):
    value: str
    is_static: bool = True
