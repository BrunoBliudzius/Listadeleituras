from PIL import Image
from io import BytesIO


def processar_imagem(conteudo: bytes) -> bytes:
    imagem = Image.open(BytesIO(conteudo))

    imagem.thumbnail((250, 375))

    buffer = BytesIO()

    imagem.save(buffer, format="WEBP", quality=100, optimize=True)

    return buffer.getvalue()
