"""melenchonPB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from callcenter import views
from callcenter.views import SampleView, AngularApp, NgTemplateView
from callcenter.views import api_user_infos, api_user_achievements, api_test_simulatecall, api_leaderboard
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns

ngurls = [
    url(r'^$', SampleView.as_view(), name='sample'),
    url(r'^ng/$', NgTemplateView.as_view(), name='ngTemplate'),
]

urlpatterns = [
    #URL AUTH
    url(r'^registerNew/', views.registerNew, name="register"),
    url(r'^registerSucess/', views.registerSucess, name="register_sucess"),

    #WEBHOOKS
    url(r'^notewebhook/$', views.noteWebhook),

    #API
        #TOKEN
    url(r'^api/token/auth/', obtain_jwt_token),
    url(r'^api/token/refresh/', refresh_jwt_token),
        #API - NO TOKEN REQUIRED
    url(r'^api/test_websocket/$', views.api_test_socket.as_view()),
    url(r'^api/simulate_call/$', views.api_test_simulatecall.as_view()),
    url(r'^api/leaderboard/(?P<ranking>\w{0,10})/$', views.api_leaderboard.as_view()),
        #API - TOKEN REQUIRED
    url(r'^api/user/infos/$', api_user_infos.as_view()),
    url(r'^api/user/achievements/$', api_user_achievements.as_view()),

    #AUTRES URLS
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include(ngurls)),

    #ANGULAR
    url(r'^(?!ng/).*$', AngularApp.as_view(), name="angular_app"),
    url(r'^ng/pokechon$', AngularApp.as_view(), name="angular_app"),
	url(r'^ng/$', AngularApp.as_view(), name="angular_app"),
] + static(settings.ANGULAR_URL, document_root=settings.ANGULAR_ROOT) + [
]
