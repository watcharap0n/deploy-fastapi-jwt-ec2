from fastapi import APIRouter, HTTPException, status
from starlette.responses import JSONResponse
from app.db import db
from typing import List
from app.schemas.user import UserInfo, UpdateUserInfo
from fastapi.encoders import jsonable_encoder

router = APIRouter()
collection = 'users'


@router.get('/', response_model=List[UserInfo], summary='Get users.')
async def get_users():
    users = await db.find(collection=collection, query={})
    users = list(users)
    return users


@router.get('/{id}', response_model=UserInfo, summary='Get query user.')
async def get_user(id: str):
    user = await db.find_one(collection=collection, query={'_id': id})
    return user


@router.post('/', response_model=UserInfo, summary='Add item')
async def add_user(payload: UserInfo):
    item_model = jsonable_encoder(payload)
    await db.insert_one(collection=collection, data=item_model)
    return payload


@router.put('/{id}', summary='Update item', response_model=UpdateUserInfo)
async def update_user(
        id: str,
        payload: UpdateUserInfo
):
    item_model = jsonable_encoder(payload)
    query = {'_id': id}
    values = {'$set': item_model}
    if (await db.update_one(collection=collection, values=values, query=query)) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not fount item to update')
    return payload


@router.delete('/{id}', summary='Delete item')
async def delete_user(id: str):
    query = {'_id': id}
    if (await db.delete_one(collection=collection, query=query)) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not fount item to delete')
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={'id': id, 'detail': 'deleted item.'})
