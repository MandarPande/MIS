from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('student/',views.student, name = "student"),
    path('achievements/', views.home),
    path('login/', views.doLogin, name="login")
  ] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

