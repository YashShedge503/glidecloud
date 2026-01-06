from bson import ObjectId
from fastapi import HTTPException
from app.db.mongodb import user_collection
from app.utils.serializers import user_helper

async def create_user(user):
    result = await user_collection.insert_one(user.dict())
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

async def get_all_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

async def get_user_by_id(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_helper(user)

async def update_user(user_id: str, user):
    updated = await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )
    if updated.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await user_collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(updated_user)

async def delete_user(user_id: str):
    deleted = await user_collection.delete_one({"_id": ObjectId(user_id)})
    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
