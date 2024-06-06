# django-jwt

### steps init project:
- `python3 -m venv env`
- `pip install -r ./requirements.txt`
- `django-admin startproject backend`
- `cd backend && python manage.py startapp api`

### docker:
```sh
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=12345Sa';" \ -p 1433:1433 --name sql1 --hostname sql1 \ -d \ mcr.microsoft.com/mssql/server:2022-latest
```