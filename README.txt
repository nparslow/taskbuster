
# virtual env for testing: tb_test

# to make a locale language set of files for the language 'ca' (catalan):
python manage.py makemessages -l ca

# once translations are added, compile them with:
python manage.py compilemessages -l ca 
