from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('blogs/', views.blogs, name="blogs"),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name = 'logout'),

    path('admissions/', include('registration.urls')),
    path('students/', include('students.urls')),
    path('adminhome',include('alimiaAdmin.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
