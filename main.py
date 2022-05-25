from docxtpl import DocxTemplate

doc = DocxTemplate('ticket_template.docx')

questions = [
    1,
    'Что такое интерпретируемые ЯП',
    'Что такое компилируемые ЯП',
    'Что такое ЯП, исполняемые в ВМ'
]

context = {
    'faculty': 'ФГиИБ',
    'department': 'ИИС',
    'year': '2021-2022',
    'questions': questions[1:],
    'date': '19.05.2022',
    'teacher': 'Бондарев И.Н.',
    'number': questions[0],
    'len_q': len(questions)-1
}
print(*questions)
doc.render(context)
doc.save('ticket1.docx')