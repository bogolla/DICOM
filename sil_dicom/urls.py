from rest_framework import routers
from .views import (
    DocumentViewSet
)

router = routers.SimpleRouter()
router.register(r'images', DocumentViewSet)

urlpatterns = router.urls
