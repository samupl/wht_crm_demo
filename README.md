# WHT CRM Demo

An example app showing how easy it is to write a simple customer table viewer/editor in Django and DataTables.

## Installation

```bash
virtualenv -p $(which python3) ~/.virtualenvs/wht_crm_demo
source ~/.virtualenvs/wht_crm_demo/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Running

You can run the test server to preview the app using `python manage.py runserver`. 

For production deployment please refer to https://docs.djangoproject.com/en/1.9/howto/deployment/

## Configuration

To configure the database, please edit _wht_crm_demo/settings.py_ according to the django documentation.

This is just a proof of concept, not an actual project, so no .ini file support has been implemented.