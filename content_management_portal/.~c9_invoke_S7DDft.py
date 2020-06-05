import requests
import json
from ib_miniprojects_backend.models.question import Question
def control_flow():

	# Login_User

	data = '{"username": "siva","password": "siva123456"}'
	url = 'http://127.0.0.1:8080/api/content_management_portal/login/v1/'
	headers = {"content-type": "application/json"}
	response = requests.get(url=url, headers=headers, data=data)
	response = json.loads(response.content)
	print(response)
	
	access_token = response['access_token']
	format = "Bearer {access_token}".format(access_token)

	#Question_creation
	
	Question.objects.all().delete()
	data = '{"short_title":"ibhubs","problem_description": {"content_type": "HTML","content": "softwaresolutions"}}'
	url = 'http://127.0.0.1:8080/api/content_management_portal/question/v1/'
	headers = {"content-type": "application/json", "Authorization": format}
	response = requests.post(url=url, headers=headers, data=data)

# print(response.content)





control_flow()