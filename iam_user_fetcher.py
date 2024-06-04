import boto3

class IAMUserFetcher:
    def __init__(self):
        self.iam_client = boto3.client('iam')
        
    def get_all_users(self):
        users = []
        paginator = self.iam_client.get_paginator('list_users')
        for page in paginator.paginate():
            for user in page['Users']:
                users.append(user['UserName'])
        return users
