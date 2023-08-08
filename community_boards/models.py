from django.db import models
from common.models import CommonModel


class Community_Board(CommonModel):

    """Community Board model"""

    class CommunityBoardKindChoices(models.TextChoices):
        FREE_BOARD = "free_board", "Free Board"
        REVIEW_BOARD = "review_board", "Review Board"
        TRADE_BOARD = "trade_board", "Trade Board"

    kind = models.CharField(
        max_length=15,
        choices=CommunityBoardKindChoices.choices,
    )

    nickname = models.CharField(
        max_length=20,
    )

    content = models.TextField()

    is_blocked = models.BooleanField(default=False)

    file = models.FileField()

    def __str__(self):
        return self.kind
