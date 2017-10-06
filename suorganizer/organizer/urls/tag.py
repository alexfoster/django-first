from django.conf.urls import url

from organizer.views import (TagCreate, TagUpdate, TagDelete, TagDetail, TagList)

# order matters
urlpatterns = [
	url(r'^tag/$', TagList.as_view(), name='organizer_tag_list'),
	url(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
	url(r'^tag/(?P<slug>[\w\-]+)/$', TagDetail.as_view(), name='organizer_tag_detail'),
	url(r'^tag/(?P<slug>[\w-]+)/delete/$', TagDelete.as_view(), name='organizer_tag_delete'),
	url(r'^tag/(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='organizer_tag_update'),
]
