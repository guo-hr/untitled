# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 18:06
# @Author  : Conderfly
# @Email   : coderflying@163.com
# @File    : login.py
import re
import base64
import requests
from server.utils.generate_check_url import generate_url
from server.utils.yundama import indetify
from server.utils.constants import s,headers


def encpyptwithXor(param):
    return [i ^ 0x5 for i in param.encode()]

def byte_to_str(alist,bolean,length ) -> list:
    res = [0 for _ in range(length * 2)]
    bo = False
    i = 0
    while i < length:
        b = alist[i + bolean] & 0xFF
        bo1 = bo + True
        res[bo] = s[b >> 4]
        bo = bo1 + True
        res[bo1] = s[b & 0xF]
        i += 1
    return res

def get_login_params(param):
    xor = encpyptwithXor(param=param)
    return "".join(byte_to_str(xor, False, len(xor)))

def douyin_login_params(mobile,password,captcha=""):
    mobile = "+86" +mobile
    mobile, password = get_login_params(mobile), get_login_params(password)
    login_params = {
        "mobile": mobile,
        "password":password,
    }
    url = generate_url("https://lf.snssdk.com/user/mobile/login/v2/?mix_mode=1",extract=login_params)
    url = re.sub(r'&mobile[\s\S]*?&as',"&as",url)
    form_data = {
        "mobile": mobile,
        "password": password,
        "mix_mode": 1,
        "retry": "no_retry",
    }
    if captcha:
        form_data["captcha"] = captcha
    return url, form_data

def login(mobile,password):
    message,captcha = "error",""
    while message != "success":
        url, form_data = douyin_login_params(mobile,password,captcha)
        response = requests.post(url,data=form_data,headers=headers,verify=False)
        response_json = response.json()
        data, message = response_json.get("data"), response_json.get("message")
        if message == "error":
            error_code = data.get("error_code")
            if error_code in [1101,1102]:
                # 验证码问题
                image_content = base64.b64decode(data.get("captcha").encode())
                captcha = indetify(image_content)
            elif error_code == 1009:
                # 密码错误
                return {"code":0,"message":"账号或密码错误。"}
            else:
                print(error_code)
        else:
            return {"code":1,"cookie":response.cookies.get_dict(),"message":response_json}


if __name__ == '__main__':
    res = login("13723731974", "123456daxia")
    print(res)
    print("input:+86199****2945")
    print("result:",get_login_params("199****2945"))
