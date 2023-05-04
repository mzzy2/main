import re
import datetime

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')

    users = []
    
    while True: 
        user = {}
        
        while True: 
            username = input("Username: ")
            hangeul = re.compile("^[ㄱ-힣]+$")
            hangeul_check = hangeul.match(username)
            if (len(username) >= 2 and len(username) <= 4 and hangeul_check):
                break
            else:
                print("이름을 2~4자 이내로 작성해주세요.")
                continue

        while True: 
            password = input("Password: ")
            if len(password) >= 8 and password[0].isupper() == True and ("!" in password or "@" in password or "#" in password or "$" in password):
                break
            else:
                print("특수문자 (!, @, #, $) 중 1가지를 포함시켜 8자 이상 작성해주세요.")
                continue

        while True: 
            email = input("email: ")
            regex_email =  r"^[a-z0-9]+?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$"
            valid = re.search(regex_email, email)
            if (email.endswith(".com") == True and "@" in email and valid):
                break
            else: 
                print("이메일의 형식이 올바르지 않습니다.")


        user["username"] = username
        user["password"] = password
        user["email"] = email
        user["stnr_date"] = stnr_date

        users.append(user)
        print([user['username'], user['password'], user['email']])

        cont = input("더 입력하시겠습니까? y/n: ")
        if (cont == "y"):
            continue
        else: 
            return users
            exit()
        
def load_to_txt(user_list):
    f = open('user.txt', 'w', encoding= 'UTF-8')
    f.close()

def run():
    user_list = create_membership()
    load_to_txt(user_list)

run()