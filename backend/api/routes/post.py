from fastapi import APIRouter, File, UploadFile, Form, Depends
from api.services.inserir_obra import inserir_obra
from conn import get_connection
from typing import Annotated

router = APIRouter()


@router.post("/", status_code=201)
async def inserir(
    titulo: Annotated[str, Form()],
    editora: Annotated[str | None, Form()] = None,
    status: Annotated[str | None, Form()] = None,
    capa: Annotated[UploadFile | None, File()] = None,
    conn=Depends(get_connection),
):
    await inserir_obra(
        titulo,
        editora,
        status,
        capa,
        conn,
    )

    return {"success": "Dados gravados!!"}
