from data_base import crud
from datetime import datetime
from my_logger import logger
import schedule
from okdeck_req_creat import create_iss_okdesk
import time

def main():
    now = datetime.now()
    start_date = now.replace(hour=10, minute=0, second=0, microsecond=0)
    end_date = now.replace(hour=17, minute=0, second=0, microsecond=0)

    try:
        db_results = crud.get_sim_to_abon(start_time=start_date, end_time=end_date)
    except Exception as e:
        logger.error(f'Ошибка загрузки данных: {e}')
        return
    else:
        if db_results:
            for sim in db_results:
                create_iss_okdesk(
                    sim_number=str(sim.sim_tel_number)
                )

# Задаем время выполнения скрипта
schedule.every().day.at("17:00").do(main)
# Бесконечный цикл для выполнения заданий
while True:
    schedule.run_pending()
    time.sleep(1)
