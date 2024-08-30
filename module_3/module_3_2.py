def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = (".com", ".ru", ".net")
    
    if "@" not in recipient or "@" not in sender:
        conclusion = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif not (recipient.endswith(valid_domains) and sender.endswith(valid_domains)):
        conclusion = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif recipient == sender:
        conclusion = "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        conclusion = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"
    else:
        conclusion = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}"
    
    print(conclusion)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender ='urban.teacher@mail.ru')