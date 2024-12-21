from rest_framework import routers

from authors.views import AuthorViewSet
from authors.apps import AuthorsConfig


app_name = AuthorsConfig.name

router = routers.DefaultRouter()
router.register(r"", AuthorViewSet, basename="author")

urlpatterns = router.urls
