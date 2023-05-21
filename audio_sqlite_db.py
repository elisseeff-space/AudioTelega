import sqlite3 as sq
from datetime import datetime
import pandas as pd 

def sql_start(logger) -> None:
    global dbase, cur
    dbase = sq.connect('audio_telega.db')
    cur = dbase.cursor()
    if dbase:
        logger.warning("audio_telega: Data base connected Ok!")
    dbase.execute('create table if not exists audio_telega_use_log(use_date TEXT, user_name TEXT, user_id TEXT, action TEXT, language_code TEXT, confidence REAL)')
    dbase.commit()

def use_log_add_command(user_name, user_id, action, language_code, confidence):
    use_date = datetime.now()
    params = (use_date, user_name, user_id, action, language_code, confidence)
    dbase.execute('insert into audio_telega_use_log values (?,?,?,?,?,?)', params)
    dbase.commit()

def sql_read() -> pd.DataFrame :
    df = pd.read_sql_query("SELECT * FROM audio_telega_use_log", dbase)
    return df

