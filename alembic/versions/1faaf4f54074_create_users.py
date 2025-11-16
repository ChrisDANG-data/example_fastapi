"""create users

Revision ID: 1faaf4f54074
Revises: e133dc81eb47
Create Date: 2025-11-13 13:20:36.819653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1faaf4f54074'
down_revision: Union[str, Sequence[str], None] = 'e133dc81eb47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
