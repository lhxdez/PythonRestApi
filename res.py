import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Test1", "views": 10}, 
        {"likes": 11, "name": "Test2", "views": 20}, 
        {"likes": 20, "name": "Test3", "views": 30}, 
        {"likes": 30, "name": "Test4", "views": 40}]


# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()


response = requests.patch(BASE + "video/2", {"views": 99, "likes": 1000})
print(response.json())