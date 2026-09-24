from conn import DB_SCHEMA, DB_TABLE
from psycopg2 import sql


async def obter_imagem(obra_id, conn):
    cursor = conn.cursor()

    try:
        cursor.execute(
            sql.SQL("""
        SELECT capa
        FROM {}.{}
        WHERE id = %s
    """).format(
                sql.Identifier(DB_SCHEMA),
                sql.Identifier(DB_TABLE),
            ),
            (obra_id,),
        )

        resultado = cursor.fetchone()

        capa = resultado[0]
        return capa

    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
