# from django.conf.urls import url
# from info import views

# urlpatterns = patterns('',
#     url(r'^/?$', 'info.views.index'),
#     (r'^static/(.*)$', 'django.views.static.serve', {'document_root':           
#     os.path.join(os.path.dirname(__file__), 'static')}),
# )

from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)