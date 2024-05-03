import uuid

from ninja import Schema


class UserSchemaInput(Schema):
    name: str
    first_name: str
    last_name: str
    email: str
    password: str


class BusinessSchemaIn(Schema):
    name: str


class LoginSchemaInput(Schema):
    email: str
    password: str


class SignInSchemaOut(Schema):
    user_id: uuid.UUID
    user_email: str
    user_role: str
    access_token: str


class RefreshTokenSchemaOut(Schema):
    access_token: str


class CurrentUserSchemaOut(Schema):
    first_name: str
    role: str
