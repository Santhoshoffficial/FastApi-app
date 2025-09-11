from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    name: str


# Create schema (what client sends when creating a role)
class RoleCreate(RoleBase):
    pass


# Update schema (for PATCH/PUT)
class RoleUpdate(RoleBase):
    pass


# Response schema (what API returns)
class RoleInDBBase(RoleBase):
    id: int

    class Config:
        orm_mode = True


# Final response schema
class Role(RoleInDBBase):
    pass


# Internal schema (with DB only fields)
class RoleInDB(RoleInDBBase):
    pass
