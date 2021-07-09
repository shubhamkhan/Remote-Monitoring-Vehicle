from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^/(?P<stream_path>(.*?))/$',views.picam_stream, name="picamstream"),
    path('ledOn/', views.ledOn, name='ledOn'),
    path('ledOff/', views.ledOff, name='ledOff'),
    path('dth/', views.dth, name="dth"),
    path('penLL/', views.panLL, name="penLL"),
    path('penL/', views.panL, name="penL"),
    path('penM/', views.panM, name="penM"),
    path('penR/', views.panR, name="penR"),
    path('penRR/', views.panRR, name="penRR"),
    path('tiltDD/', views.tiltDD, name="tiltDD"),
    path('tiltD/', views.tiltD, name="tiltD"),
    path('tiltM/', views.tiltM, name="tiltM"),
    path('tiltU/', views.tiltU, name="tiltU"),
    path('tiltUU/', views.tiltUU, name="tiltUU"),
    path('forward/', views.forward, name="forward"),
    path('stop/', views.stop, name="stop"),
    path('backward/', views.backward, name="backward"),
    path('left/', views.left, name="left"),
    path('right/', views.right, name="right"),    
]