# coding=utf-8

from sqlalchemy import Column, String

from .entity import Entity, Base

from marshmallow import Schema, fields

### Existing state, output from boat.
class ExistingState(Entity, Base):
    __tablename__ = 'ExistingStates'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

class ExistingStateSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    updated_at = fields.DateTime()
    windSpeed = fields.Number()
    windDirection = fields.Number()
    boatSpeed = fields.Number()
    boatDirection = fields.Number()
