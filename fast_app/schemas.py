from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    text: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr  # Class do pydantic para validar email
    password: str


class UserPublicSchema(BaseModel):
    username: str
    email: EmailStr
    id: int


class DbUserSchema(UserSchema):
    id: int


class UsersList(BaseModel):
    users: list[UserPublicSchema]
