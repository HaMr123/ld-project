
list = [{"name": "推荐食谱", "1": "症状", "name1": "浑身忽冷忽热"}, {"name": "绿豆薏米饭"}, {"name": "芝麻"}]
# res = [item[key] for item in list for key in item]
res = [item[key] for item in list for key in item ]
#print(res)

data = {'Uid': '12600742b9046b92dd218378d85b63a5',
        'Message': '成功',
        'Token': 'd00cNs4dAhY9VwJJdFhgQI',
        'Code': 10000,
        'Result': {
                   'hierarchyType': 'GS',
                   'companyName': '测试',
                   'operateId': '1911130B72735D68F3',

                   'companyId': '191128F82E30EEA73C',
                   'roleName': '公司管理员',
                   'username': 'gcs'
                   }
        }
print(data['Result'])







