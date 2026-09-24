from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from io import BytesIO

from api.services.processar_imagem import processar_imagem


async def verifica_arquivo(capa: UploadFile | None) -> bytes | None:
    if capa is None:
        return None

    extensao = Path(capa.filename).suffix.lower()

    if extensao != ".webp":
        raise HTTPException(
            status_code=400,
            detail="Formato não suportado, somente WebP",
        )

    conteudo = await capa.read()

    MAX_SIZE = 5 * 1024 * 1024

    if len(conteudo) > MAX_SIZE:
        raise HTTPException(
            status_code=400,
            detail="A imagem não pode ter mais de 5 MB",
        )

    try:
        imagem = Image.open(BytesIO(conteudo))

        if imagem.format != "WEBP":
            raise HTTPException(
                status_code=400,
                detail="O arquivo não é uma imagem WebP válida",
            )

        imagem.verify()

    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="O arquivo enviado não é uma imagem válida",
        )

    return processar_imagem(conteudo)
