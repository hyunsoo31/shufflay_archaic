"""shufflay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin



from web.views import main
from web.views import index
from web.views import account
from web.views import library
from web.views import bgm
from web.views import photo
from web.views import hot
from web.views import community, new, create
from web.views import upload
from web.views import customer
from web.views import team
from web.views import bgm2
from web.views import signup
from web.views import login
from web.views import logout
from web.views import photo_animal, photo_building, photo_emotion, photo_food, photo_music, photo_nature, photo_people, photo_sport
from web.views import upload_file

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name="home"),
    url(r'^hyunsoo', index, name="hyunsoo"),
    url(r'^account/', account, name="account"),
    url(r'^library/', library, name="library"),
    url(r'^bgm/', bgm, name="bgm"),
    url(r'^photo/', photo, name="photo"),
    url(r'^hot/', hot, name="hot"),
    url(r'^community/', community, name="community"),
    url(r'^new/', new, name="new"),
    url(r'^create/', create, name="create"),
    #url(r'^community/(?P<blog_id>/[0-9]+)', detail, name="detail"),
    url(r'^upload/', upload, name="upload"),
    url(r'^customer/', customer, name="customer"),
    url(r'^team/', team, name="team"),
    url(r'^bgm2/', bgm2, name="bmg2"),
    url(r'^signup/', signup, name="signup"),
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^photo_animal/', photo_animal, name="photo_animal"),
    url(r'^photo_building/', photo_building, name="photo_building"),
    url(r'^photo_emotion/', photo_emotion, name="photo_emotion"),
    url(r'^photo_food/', photo_food, name="photo_food"),
    url(r'^photo_music/', photo_music, name="photo_music"),
    url(r'^photo_nature/', photo_nature, name="photo_nature"),
    url(r'^photo_people/', photo_people, name="photo_people"),
    url(r'^photo_sport/', photo_sport, name="photo_sport"),
    url(r'^upload_file/', upload_file, name="upload_file"),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)