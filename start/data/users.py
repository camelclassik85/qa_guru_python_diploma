from pydantic import BaseModel


class User(BaseModel):
    email: str = ''
    password: str = ''
    phone: str = ''
    auth: str = ''
    default_profile_id: str = ''


authorized_user = User(
    email='qagdiploma@qa.qa',
    password='111111',
    auth='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI2NjIzOGFiZjcxYjkxYzM1'
         'MWM5MGYzNzQiLCJwaWQiOiIxZmY3NzYzMi0yNzY3LTQ5MTctOTUwYy1iMjBmNWZiOGU0Z'
         'mMiLCJkaWQiOiIyNzE1MGNiOS1iMDBiLTQ1ZjEtODhiOC0zY2NiZGZkNWZlODQiLCJhbm'
         '9ueW1vdXMiOmZhbHNlLCJmb3Jfa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2l'
         'zdGVyZWQiLCJhY2xfZXhwaXJlIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzEzNzMzNTc4LCJ2'
         'IjozfQ.WhiN4Cso1Q3d2y-b549l4L3jjsfecNVd_SDN0DP7AOQ'
    )
