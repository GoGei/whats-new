from django.conf.urls import url, include

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
]
