from api.services.pesquisar_banco import pesquisar_banco
from api.services.obter_imagem import obter_imagem
from fastapi import APIRouter, Depends, Response
from conn import get_connection

router = APIRouter()


@router.get("/")
async def Visualizar(conn=Depends(get_connection)):
    dados = await pesquisar_banco(conn)
    return dados


@router.get("/{obra_id}/capa")
async def obter_capa(obra_id: int, conn=Depends(get_connection)):
    capa = await obter_imagem(obra_id, conn)
    return Response(content=capa, media_type="image/webp")
