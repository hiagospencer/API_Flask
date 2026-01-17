from marshmallow import Schema, fields, validate

class CreateUserSchema(Schema):
    name = fields.String(
        required=True, validate=validate.Length(min=2)
    )
    email = fields.Email(required=True)
    
class UserResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()