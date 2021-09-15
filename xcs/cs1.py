


datas = {
  "test_1":{"url":"http://test.hyunst.com/ht/login_staffLogin.do",
            "user":"gcs",
            "pswd":"E10ADC3949BA59ABBE56E057F20F883E",
            "result": "成功",
            "resultcode": 200},
  "test_2": {"url":"http://test.hyunst.com/ht/login_staffLogin.do",
            "user":"dd",
            "pswd":"",
            "result": "密码不能为空！",
            "resultcode": 200},
  "test_3": {"url":"http://test.hyunst.com/ht/login_staffLogin.do",
            "user":"",
            "pswd":"E10ADC3949BA59ABBE56E057F20F883E",
            "result": "用户名不能为空！",
            "resultcode": 200}
}
hh =
# 语法：dict.values(),字典 values()方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
for data in datas.values():


    hh.append((data))
    print(hh)
    for gg in hh.values():
        print(gg)


print(gg)
    # for arrs in data.values():
    #     hh.append((arrs))
    #     print(hh)





