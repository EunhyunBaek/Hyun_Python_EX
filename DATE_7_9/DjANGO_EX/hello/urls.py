from django.conf.urls import url
from . import views # views는 위에서 작성한 views.py가 들어 있는 폴더
# url 패턴 추가
urlpatterns = [
	url(r'^$', views.index, name='index'),
]