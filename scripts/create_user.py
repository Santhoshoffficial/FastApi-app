import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import SessionLocal
from app.models.users import User
from app.models.role import Role
from passlib.context import CryptContext
from sqlalchemy import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(email: str, password: str, role_name: str):
    async with SessionLocal() as session:
        # 1. Check if role exists using ORM query
        result = await session.execute(select(Role).where(Role.name == role_name))
        role_obj = result.scalars().first()

        if not role_obj:
            role_obj = Role(name=role_name)
            session.add(role_obj)
            await session.commit()
            await session.refresh(role_obj)

        # 2. Hash password
        hashed_password = pwd_context.hash(password[:72])

        # 3. Create user
        user = User(
            email=email, hashed_password=hashed_password, user_role_id=role_obj.id
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

        print(f"User created with id: {user.id} and email: {user.email}")


if __name__ == "__main__":
    asyncio.run(create_user("admin@yopmail.com", "1234", "admin"))
