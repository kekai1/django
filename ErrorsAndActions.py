# pymysql.err.DataError: (1406, "Data too long for column 'url' at row 1")
#SET @@global.sql_mode= '';  - В воркбэнч делаем sql-запрос

'''
Если есть проблемы с виртуальным окружением
Решение проблемы:
- Открываем терминал PowerShell от админа.
- Пишем: Set-ExecutionPolicy RemoteSigned
- На вопрос отвечаем - A
'''



#actions

#   .\venv\Scripts\activate
#   cd mysite
#   python manage.py runserver

#options:
# pip list



'''
Обработка исключений: 
    handler500 - ошибка сервера
    handler404 - странциа не найдена
    handler403 - доступ запрещен
    handler400 - невозможно обработать запрос
'''


'''
Шаблонные фильтры jinja2 - https://djbook.ru/rel3.0/ref/templates/builtins.html#ref-templates-builtins-filters
'''