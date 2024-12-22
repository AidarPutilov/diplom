from rest_framework import routers

from books.views import BookViewSet
from books.apps import BooksConfig


app_name = BooksConfig.name

router = routers.DefaultRouter()
router.register(r"", BookViewSet, basename="book")

urlpatterns = router.urls
