"""compareapp3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Product_ListView,name="home"),
    path('fashion/',views.Pfashion_view,name="fashion"),
    path('electronics/',views.Pelectronic_view,name="electronic"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Product_ListView,name="product_tag"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Pelectronic_view,name="product_tag"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Pfashion_view,name="product_tag"),
    path('trends/',views.news_view,name="trends"),
    path('tag/(?p<tag_slug>[-\w]/$',views.news_view,name="news_tag"),
    path('sports/',views.Psports_view,name="sports"),
    path('national/',views.news_national,name="national"),
    path('international/',views.news_international,name="international"),
    path('youtube/',views.youtube_view,name="youtube"),
    path('others/',views.Pother_view,name="others"),
    path('fashionnbeauty/',views.ybeuty_view,name="fb"),
    path('education/',views.yedu_view,name="education"),
    path('gaming/',views.ygaming_view,name="gaming"),
    path('vlogs/',views.yvlog_view,name="vlogs"),
    path('entertainment/',views.yenter_view,name="entertainment"),
    path('sportz/',views.ysports_view,name="sportz"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.Signup_view),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)