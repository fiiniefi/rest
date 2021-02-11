from pydantic import BaseModel


class Hypermedia(BaseModel):
    _links: dict
