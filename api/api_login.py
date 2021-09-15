import requests


class ApiLogin(object):

    def api_post_login(self,url,user,pswd):
        url = "http://test.hyunst.com/ht/login_staffLogin.do"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        Params = {"username":user,"password":pswd}
        body = {"Api": "doLogin",
                "Params": str(Params),
                "ClientId": "100122",
                "Timestamp":"1616743602133"
        }
        return requests.post(url,headers = headers,data=body)

if __name__ == '__main__':
    url = "http://test.hyunst.com/ht/login_staffLogin.do"
    user = "gcs"
    pswd = "E10ADC3949BA59ABBE56E057F20F883E"

    s = ApiLogin().api_post_login(url,user,pswd)
    print(s.json())

