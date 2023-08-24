from django.conf.urls import url, include
from Manager.Api.urls import urlpatterns as api_urls

urlpatterns = [
    url(r'', include('urls')),
    url(r'^', include('Manager.Login.urls')),
    url(r'^', include('Manager.Home.urls')),
    url(r'^users/', include('Manager.Users.urls')),
    url(r'^admins/', include('Manager.Admins.urls')),
    url(r'^author-requests/', include('Manager.AuthorRequest.urls')),
    url(r'^subscriptions/', include('Manager.Subscription.urls')),
    url(r'^category-colors/', include('Manager.CategoryColors.urls')),
    url(r'^post-colors/', include('Manager.PostColors.urls')),
    url(r'^contacts/', include('Manager.Contacts.urls')),
    url(r'^user-feedback/', include('Manager.UserFeedback.urls')),
    url(r'^categories/', include('Manager.Category.urls')),
    url(r'^posts/', include('Manager.Post.urls')),

    url(r'^api/', include((api_urls, 'manager-api-v1'), namespace='manager-api-v1')),
]
