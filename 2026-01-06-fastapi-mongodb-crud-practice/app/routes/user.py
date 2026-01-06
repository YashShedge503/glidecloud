from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

router = APIRouter()

# CREATE
@router.post("/", response_model=dict)
async def create(user: User):
    return await create_user(user)

# READ ALL
@router.get("/", response_model=list)
async def read_all():
    return await get_all_users()

# READ ONE
@router.get("/{user_id}", response_model=dict)
async def read_one(user_id: str):
    return await get_user_by_id(user_id)

# UPDATE
@router.put("/{user_id}", response_model=dict)
async def update(user_id: str, user: User):
    return await update_user(user_id, user)

# DELETE
@router.delete("/{user_id}")
async def delete(user_id: str):
    return await delete_user(user_id)
