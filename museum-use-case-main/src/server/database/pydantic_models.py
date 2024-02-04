from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 1


class ArtistModel(ModifyBaseModel):
    name: str
    birth_date: str
    nationally: str
    style: str

class ExhibitModel(ModifyBaseModel):
    artist_id: int
    name: str
    description: str
    date_acquired: str

class ExhibitCuratorModel(ModifyBaseModel):
    exhibit_id: int
    curator_id: int

class CuratorModel(ModifyBaseModel):
    name: str
    department: str

class ExhibitLocationModel(ModifyBaseModel):
    exhibit_id: int
    room_number: str
    floor: str

class ExhibitCollectionModel(ModifyBaseModel):
    collection_id: int
    exhibit_id: int

class CollectionModel(ModifyBaseModel):
    name: str
    description: str

class EventModel(ModifyBaseModel):
    name: str
    date: str
    description: str

class VisitorModel(ModifyBaseModel):
    name: str
    email: str
    membership_status: str

class TicketModel(ModifyBaseModel):
    visitor_id: str
    date_purchased: str
    price: str





