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
    auth='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI2NjIzOGFiZjcxYjkxYzM1MWM5MG'
         'YzNzQiLCJwaWQiOiIxZmY3NzYzMi0yNzY3LTQ5MTctOTUwYy1iMjBmNWZiOGU0ZmMiLCJkaWQiO'
         'iJlZmUzMzU2Yy00OTU0LTQ5MDQtYjRkYi01NTUxYzQ1N2RmMTQiLCJhbm9ueW1vdXMiOmZhbHNl'
         'LCJmb3Jfa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2lzdGVyZWQiLCJhY2xfZXhwaXJ'
         'lIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzE0MjA3NTIyLCJ2IjozfQ.i-gD_X2JzsXyVrIofcK-UL-'
         'uLTgN910j9IoZy0zSC1I',
    default_profile_id='1ff77632-2767-4917-950c-b20f5fb8e4fc'
    )
