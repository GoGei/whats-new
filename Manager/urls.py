from django.conf.urls import url, include
from Api.routers import admin_routers

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

    url(r'^api/v1/', include((admin_routers.router_v1.urls, 'api-admin-v1'), namespace='api-admin-v1')),
]
