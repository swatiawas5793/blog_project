"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name = "post_list"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^login/$', views.user_login, name ="user_login"),
    url(r'^logout/$', views.user_logout, name ="user_logout"),
    url(r'^register/$', views.register, name = "register"),

    # password reset url'
    #url(r'^password-reset/$', auth_views.password_reset, name ="password_reset"),
    #url(r'^password-reset/done/$', auth_views.password_reset_done, name ="password_reset_done"),
    #url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name="password_reset_confirm"),
    #url(r'^password-reset/confirm/(?p<uidb64>[\w-]+)/(?p<token>[\w-]+)/$', auth_views.password_reset_confirm, name ="password_reset_confirm"),
     #url(r'^password-reset/complete$', auth_views.password_reset_complete, name ="password_reset_complete"),
     url(r'^',include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
