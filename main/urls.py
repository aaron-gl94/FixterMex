from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.Home.as_view(),name='home'),
	url(r'^movie/(?P<id>\d+)/$',views.DetailMovie.as_view(),name="detail_movie"),
	url(r'^cines/$',views.CineList.as_view(),name='cines'),
	url(r'^cine/(?P<id>\d+)/$',views.DetailCine.as_view(),name="detail_cine"),
	url(r'^horarios/$',views.TimeList.as_view(),name="horarios"),
	url(r'^horario/(?P<id>\d+)/$',views.DetailTime.as_view(),name="detail_time"),

]