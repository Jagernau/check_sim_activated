from okdesc_class import OkdeskClass
from config import OK_TOKEN, OK_URL
from my_logger import logger

def create_iss_okdesk(
        sim_number
        ):
    try:
        ok_class = OkdeskClass(OK_URL, OK_TOKEN)

        text_title = f"Активация сим {sim_number} без привязанного терминала"
        text_descr = f'Сим карта {sim_number} перешла из первичной блокировки в АКТИВНЫЙ, но в СИМ не прописан IMEI терминала и нет КЛИЕНТА'

        ok_class.create_issues(
                title=text_title, 
                description=text_descr,
                company_id=str(63), 
                assignee_id=str(2), 
                maintenance_entity_id=None, 
                type_iss="inner"
                )

    except Exception as e:
        logger.error(f'Не удалось создать заявку на сим {sim_number}, ошибка {e}')

