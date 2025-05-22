import requests


class YouGileApi:

    # Инициализация
    def __init__(self, url):
        self.url = url
        # Получить токен
        # Подставить свои значения в поля login, password, companyId
        token_payload = {
            "login": 'EMAIL',
            "password": 'PASSWORD',
            "companyId": 'COMPANY_ID'
            }
        token_headers = {"Content-Type": "application/json"}
        response = requests.post(self.url + '/auth/keys/get',
                                 json=token_payload, headers=token_headers)
        resp = response.json()
        token = resp[-1].get("key")
        self.token = token

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
            }
        self.headers = headers

    # Получить список проектов
    def get_projects_list(self):
        response = requests.get(self.url + '/projects', headers=self.headers)
        return response.json()["content"]

    # Создать проект
    def create_project(self, payload):
        response = requests.post(f"{self.url}/projects",
                                 json=payload, headers=self.headers)
        return response

    # Получить проект по ID
    def get_project_by_id(self, new_id):
        response = requests.get(f"{self.url}/projects/{new_id}",
                                headers=self.headers)
        return response

    # Изменить проект
    def update_project(self, project_id, payload):
        response = requests.put(f"{self.url}/projects/{project_id}",
                                json=payload, headers=self.headers)
        return response
