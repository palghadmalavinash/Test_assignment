import requests
import configparser


class git_api(object):

    def __init__(self):
        self.settings = configparser.RawConfigParser()
        self.settings._interpolation = configparser.ExtendedInterpolation()
        self.settings.read(r"config/config.ini")
        self.url = self.settings.get('URL',"gitapi")
        self.accesstoken = self.settings.get("CRED",'access_token')

    def create_rep(self,repo_name):
        """
        Core function that creates the repo on GIT
        :param repo_name: Name of the repo to be created
        :return: response of create request
        """
        data = {
                 "name": repo_name,
                 "description": "This is your first repository",
                 "homepage": "https://github.com",
                 "private": False,
                 "has_issues": True,
                 "has_projects": True,
                 "has_wiki": True
                }
        payload={
            "access_token":self.accesstoken
        }
        headers={'Content-Type': "application/json", 'Accept': "application/json"}
        create_request = self.url+"user/repos"
        req_url = requests.post(create_request,
                                json=data,
                                params=payload,
                                verify=False,
                                headers=headers)
        return req_url

    def star_repo(self,create_repo):
        """
        Core function to star a repo on GIT
        :param create_repo: Response from create repo request
        :return: response of star request
        """
        response_data=create_repo.json()
        repo_fullname=response_data["full_name"]
        payload = {
            "access_token": self.accesstoken
        }
        headers = {'Content-Type': "application/json", 'Accept': "application/json"}
        create_url=self.url+"user/starred/"+repo_fullname
        req_url = requests.put(create_url,
                                params=payload,
                                verify=False,
                                headers=headers)
        return req_url

    def validate_repo(self,create_repo):
        """
        Core function to get the starred repo and validate
        :param create_repo: Response from create repo request
        :return: Bool
        """
        response_data = create_repo.json()
        repo_fullname = response_data["full_name"]
        payload = {
            "access_token": self.accesstoken
        }
        headers = {'Content-Type': "application/json", 'Accept': "application/json"}
        create_url=self.url+"user/starred"
        req_url=requests.get(create_url,
                             params=payload,
                             headers=headers)
        data = req_url.json()
        text = next((repo for repo in data if repo["full_name"]==repo_fullname),False)
        if text != False:
            text=True
        return text
