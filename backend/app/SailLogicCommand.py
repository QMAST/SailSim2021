# coding=utf-8

from sqlalchemy import Column, String

from .entity import Entity, Base, CommandEntity

from marshmallow import Schema, fields

class SailLogicCommand(CommandEntity, Base):
    __tablename__ = 'SailLogicCommand'

    def __init__(self, commandID, commandValue, created_by):
        CommandEntity.__init__(self, created_by, commandID, commandValue)
    
### Sail commands, input to boat.
class SailLogicCommandSchema(Schema):
    id = fields.Number()
    commandID = fields.Str()
    commandValue = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
