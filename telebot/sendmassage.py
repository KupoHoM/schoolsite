import requests
from .models import TeleSettings
from Teachers.models import Teachers
from Discipline.models import Discipline
from Lessons.models import Lessons


def sendtelegram(tg_title, tg_teacher, tg_user, tg_discipline, tg_lesson):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        tg_teacher = Teachers.objects.get(id=tg_teacher)
        tg_discipline = Discipline.objects.get(id=tg_discipline)
        tg_lesson = Lessons.objects.get(id=tg_lesson)

        if text.find('{'):
            text = text.replace('tg_title', tg_title)
            text = text.replace('tg_discipline', str(tg_discipline))
            text = text.replace('tg_lesson', str(tg_lesson))
            text = text.replace('tg_teacher', str(tg_teacher))
            text = text.replace('tg_user', str(tg_user))
            # newtext = ""
            # for i in text:
            #     if (i not in ['{', '}']):
            #         newtext = newtext + i

        # else:
        #     newtext = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text
            })
        # except:
        #     pass

        finally:
            if req.status_code != 200:
                print("Ошибка отправки!")
            elif req.status_code == 500:
                print("Ошибка 500!")
            else:
                print('Сообщение отправлено!')
    else:
        pass
