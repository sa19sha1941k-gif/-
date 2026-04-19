list = [
    {
    "question": '1.В каком году была выпущена Mafia II',
    "answer": 'A.2010, B.2000, C.2013',
    "right": 'A',
    },
    {
    "question": '2.Какая игра считается отцом всех шутеров',
    "answer": 'A.Doom, B.Wolfenstein, C.GTA ',
    "right": 'A',
    },
    { "question": '3.Какая компания создала серию GTA',
      "answer":'A.Ubisoft, B.Rockstar, C.2K',
      "right":'B',

    },
    {
"question": '4.Какая из игр - сюжетная?',
      "answer":'A.Call of Duty, B.CS 2, C.PUBG',
      "right":'A',
    },
{
"question": '6.Какая компания создала серию игр Assassins Creed',
      "answer":'A.Ubisoft, B.Overkill, C.Activision',
      "right":'A',
    },
{
"question": '7.В каком году вышла Payday 2?',
      "answer":'A.2010, B.2012, C.2013',
      "right":'C',
    },
{
"question": '8.Какая из игр - бывший эксклюзив Xbox 360?',
      "answer":'A.Halo 3, B.Spider Man 3, C.GTA 3',
      "right":'A',
    },
{
"question": '9.Кто является главным героем Mafia I?',
      "answer":'A.Томми Версетти, B.Вито Скалетта, C.Томми Анджело',
      "right":'C',
    },
{
"question": '10.Какая игра про 2-ую мировую войну?',
      "answer":'A.Wolfenstein, B.Call of duty WW2, C.Все варианты верны',
      "right":'C',
    }
]
score = 0
for i in list:
    print(f"Вопрос: {i['question']}")
    print(f"Ответ: {i['answer']}")
    answer = input("Ваш ответ: ")
    if answer == i["right"]:
        print('Верно')
        score += 1
    else:
        print('Неверно')
        print (f'Верный ответ:{i["right"]}')

print(score)
match score:
    case 0:
        print("Invalid error")
    case 1:
        print("Tupoi error")
    case 2:
        print("Ploho Error")
    case 3:
        print("Norm Error")
    case 4:
        print("Good Status")
    case 5:
        print("Molodec Status")





