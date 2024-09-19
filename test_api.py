import os
import json
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def_repo_name = os.getenv("repo_name")
# input_repo_name = input('Впишите имя репозитория: ')

def check_repo():
    is_repo = requests.get(f'https://api.github.com/repos/{os.getenv("username")}/{def_repo_name}')
    print('Проверка...')
    if(is_repo.status_code == 200):
        print('Репозиторий существует')
        return True
    else: 
        print (f'Репозиторий "{def_repo_name}" не существует...')
        return False

def get_file():
    text = 'Hi, this is a test assignment.'.encode('utf-8')
    base64_text = base64.b64encode(text).decode('utf-8')
    return {'path':'', 'message':'Function get_readmefile()', 'content':base64_text}

def add_repo():
    if not check_repo():
        requests.post(f'https://api.github.com/user/repos', data=json.dumps({'name':def_repo_name}), auth=(os.getenv('username'), os.getenv('TOKEN')), headers={"Content-Type": "application/json"})
        print('Репозиторий добавлен')
        resfile = get_file()
        requests.put(f'https://api.github.com/repos/{os.getenv("username")}/{def_repo_name}/contents/FILE.md', json.dumps(resfile), auth=(os.getenv('username'), os.getenv('TOKEN')), headers={"Content-Type": "application/json"})
    
def del_repo():
    if check_repo():
        requests.delete(f'https://api.github.com/repos/{os.getenv("username")}/{def_repo_name}', auth=(os.getenv('username'), os.getenv('TOKEN')), headers={"Content-Type": "application/json"})
        print('Репозиторий успешно удален')

while True:    
    try:    
        action = int(input('\nВыберите действие, которое хотите выполнить:\n1. Добавить\n2. Удалить\n3. Выйти\nВпишите: '))
        if(action==1):
            add_repo()
        elif(action==2): del_repo()
        elif(action==3): break
        else: print('Ошибка! Необходимо вписать номер конкретного действия')
    except:
        print('Ошибка!')