import requests


class YougileApi:
    def __init__(self, url):
        self.url = url

# получение ключа
    def get_token(self, login, password, companyId):
        creds = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + "/auth/keys", json=creds)
        return resp.json()["key"]

# создание проекта
    def create_project(self, title, token):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": title
        }
        resp = requests.post(self.url + "/projects", json=data, headers=headers)
        return resp.json()

# получение проекта
    def get_project(self, project_id, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        resp = requests.get(self.url + f"/projects/{project_id}", headers=headers)
        return resp.json()

# изменение проекта
    def update_project(self, project_id, new_title, token):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": new_title
        }
        resp = requests.put(self.url + f"/projects/{project_id}", json=data, headers=headers)
        return resp.json()

# получение списка проектов
    def get_projects_list(self, token):
        """Получает список всех проектов"""
        headers = {
            "Authorization": f"Bearer {token}"
        }
        resp = requests.get(self.url + "/projects", headers=headers)
        return resp.json()
