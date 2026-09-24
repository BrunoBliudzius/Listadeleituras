from conn import DB_SCHEMA, DB_TABLE
from psycopg2 import sql


async def pesquisar_banco(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("""SELECT id, titulo, editora, status FROM {}.{}""").format(
                sql.Identifier(DB_SCHEMA),
                sql.Identifier(DB_TABLE),
            ),
        )

        obras = cursor.fetchall()

        return [
            {
                "id": obra[0],
                "titulo": obra[1],
                "editora": obra[2],
                "status": obra[3],
                "capa_url": f"/obras/{obra[0]}/capa",
            }
            for obra in obras
        ]

    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
