from django.conf.urls import url, include

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('snippets.urls')),
]