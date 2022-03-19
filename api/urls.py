from rest_framework import routers
from .views import UserViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', PostViewSet)
router.register(r'rates', PostViewSet)

urlpatterns = router.urls
