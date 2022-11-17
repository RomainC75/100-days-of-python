import requests
import datetime as dt
# USERNAME = "romrom"
# TOKEN = "mlkfjze°0987023984"

USERNAME = "romromrom"
TOKEN = "mlkfjze0987023984"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

#register
# register_raw_ans = requests.post(pixela_endpoint,json=user_params)
# register_raw_ans.raise_for_status()
# print("==>",register_raw_ans.text)


pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
create_graph_data={
    "id":"graph1",
    "name":USERNAME,
    "unit":"commit",
    "type":"float",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN
}
#create graph
# create_graphs_raw_ans = requests.post(url=pixela_graph_endpoint, json=create_graph_data, headers=headers)
# print("==>",create_graphs_raw_ans.text)

today=dt.datetime.now()
formated_date=today.strftime("%Y%m%d")
print(formated_date)

edit_graph={
    "date":formated_date,
    "quantity":"80"
}

pixela_edit_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# add a pixel
# edit_raw_ans = requests.post(url=pixela_edit_graph_endpoint, json=edit_graph,headers=headers)
# print("post",edit_raw_ans.text)

#update a pixel
put_data={
    "quantity":"1"
}
pixela_edit_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formated_date}"
# edit_raw_ans = requests.put(url=pixela_edit_graph_endpoint, json=put_data,headers=headers)
# print("put: ", edit_raw_ans)

#delete a pixel
# delete_raw_ans = requests.delete(url=pixela_edit_graph_endpoint, headers=headers)
# print("delete : ", delete_raw_ans.text)
