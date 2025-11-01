import serverless_wsgi
from backend.wsgi import application

def handler(event, context):
    return serverless_wsgi.handle(application, event, context)
