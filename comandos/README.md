# Agenda - Comandos

```python
# Executando: 
# python manage.py runserver

# Criando ambiente virtual e
# iniciando projeto Django

# https://docs.djangoproject.com/pt-br/4.2/


python -m venv venv
venv/Scripts/Activate
pip install django
django-admin startproject project .
python manage.py startapp contact


# Configurando git


git config --global user.name ''
git config --global user.email ''
git config --global init.defaultBranch main

git init
git add .
git commit -m 'first commit'

Push "save" files:
git push -u origin main


# Migrando a base de dados do Django


# Sempre executar após alterar models ou qualquer item no banco de dados
python manage.py makemigrations # cria contatos de migração
python manage.py migrate # migra contatos de migração

# Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py chancepassword USERNAME
```
