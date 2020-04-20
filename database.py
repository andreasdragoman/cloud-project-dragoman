import datetime
import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = mysql.connector.connect(user="DragomanDbUser@cloud-project-serverdb", password={Portocale1}, host="cloud-project-serverdb.mysql.database.azure.com", port=3306, database={cloudcomputing})


def create_table_translations():
    with db.connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS translations "
            "( id SERIAL NOT NULL PRIMARY KEY,"
            "  time_cast timestamp NOT NULL, "
            "  initial_language TEXT NOT NULL, "
            "  target_language TEXT NOT NULL, "
            "  initial_text TEXT,"
            "  translated_text TEXT"
            "  );"
        )


def get_all_translations():
    translations = []
    with db.connect() as conn:
        translations_db = conn.execute(
            "SELECT id, time_cast, initial_language, target_language, initial_text, translated_text "
            "FROM translations "
            "ORDER BY time_cast"
        ).fetchall()
        for row in translations_db:
            translations.append({"id": row[0],
                                 "time_cast": row[1],
                                 "initial_language": row[2],
                                 "target_language": row[3],
                                 "initial_text": row[4],
                                 "translated_text": row[5]})
    return translations


def insert_translation(initial_language, target_language, initial_text, translated_text):
    time_cast = datetime.datetime.utcnow()
    stmt = sqlalchemy.text(
        "INSERT INTO translations (time_cast, initial_language, target_language, initial_text, translated_text)" 
        " VALUES (:time_cast, :initial_language, :target_language, :initial_text, :translated_text)")
    try:
        with db.connect() as conn:
            conn.execute(stmt, time_cast=time_cast,
                         initial_language=initial_language,
                         target_language=target_language,
                         initial_text=initial_text,
                         translated_text=translated_text)
    except Exception as e:
        logger.exception(e)
        return False
    return True

