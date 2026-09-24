from fastapi import UploadFile
from api.services.verifica_arquivo import verifica_arquivo
from conn import DB_SCHEMA, DB_TABLE
from psycopg2 import sql


async def inserir_obra(titulo: str, editora: str, status: str, capa: UploadFile, conn):
    cursor = conn.cursor()

    try:
        conteudo = await verifica_arquivo(capa)

        cursor.execute(
            sql.SQL("""
                    INSERT INTO {}.{} (titulo, editora, status, capa)
                    VALUES (%s, %s, %s, %s)
                """).format(
                sql.Identifier(DB_SCHEMA),
                sql.Identifier(DB_TABLE),
            ),
            (titulo, editora, status, conteudo),
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
