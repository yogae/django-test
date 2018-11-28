"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# 장고와 웹 서버를 연결하는 데 필요한 파일
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


# 객체명은 반드시 application이어야 합니다.
# application 객체는 아파치와 같은 운영 웹 서버뿐만 아니라 장고의 개발용 웹 서버인 runserver에서도 같이 사용하는 객체입니다.
# NGINX/uWSGI는 설정 파일에서 지정한다.(httpd.conf or uwsgi.ini에서 설정)
# 개발용 runserver에서는 setting 모듈의 WSGI_APPLICATION 변수로 지정

# wsgi 모듈이 실행되는 시점에 WSGIHandler 객체가 생성되어 application 변수에 할당됩니다.
# WSGIHandler 객체를 WAS 서버가 호출하는 것입니다.
application = get_wsgi_application()
