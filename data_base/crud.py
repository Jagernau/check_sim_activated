from data_base.db_conectors import MysqlDatabase
from data_base import mysql_models_two as mysql_models
from sqlalchemy import case, literal
import sys
sys.path.append('../')
from check_objects.my_logger import logger


def get_sim_to_abon(start_time, end_time):
    """
    Возвращает сим карты у которых поменялся статус с первичной блокировки на активна,
    """
    db = MysqlDatabase()
    session = db.session
    try:
        obj_info = session.query(
                mysql_models.SimCards
            ).join(
                mysql_models.GlobalLogging,
                mysql_models.SimCards.sim_id == mysql_models.GlobalLogging.edit_id
            ).filter(
                mysql_models.GlobalLogging.section_type == "sim_card",
                mysql_models.GlobalLogging.new_value == "1",
                mysql_models.GlobalLogging.change_time >= start_time,
                mysql_models.GlobalLogging.change_time <= end_time,
                mysql_models.GlobalLogging.action == "update",
                mysql_models.GlobalLogging.old_value == "3",
                mysql_models.SimCards.terminal_imei == None

            ).all()
        return obj_info 
    except Exception as e:
        logger.error(f"Ошибка при получении информации по новым объектам: {e}")
        return None
    finally:
        session.close()


