import csv
import json
import os
#gupiaoName = input("Enter the gupiaoCode")
#print(gupiaoName)

#jsonFile = gupiaoName + ".json"
path = "D:\gupiaospider\京东方Ａ.json"
with open(path,'r') as load_f:
      load_dict = json.load(load_f)
      for i in range(len(load_dict[0])):
        #(type(load_dict[0][i]))
        print(load_dict[0][i])
        list(load_dict[0][i].values())
        # 打开文件，追加a
        out = open('京东方Ａ.csv', 'a', newline='')
        # # 设定写入模式
        csv_write = csv.writer(out, dialect='excel')
        # # 写入具体内容
        csv_write.writerow(load_dict[0][i].values())
        print("write over")



    #print(load_dict)


#json_str = json.dumps(gupiaoName+".json")
