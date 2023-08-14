from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    author = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rreviews"
    )
    board = models.ForeignKey(
        "community_boards.Board", on_delete=models.CASCADE, related_name="rreviews"
    )
    content = models.CharField(max_length=140)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.content
