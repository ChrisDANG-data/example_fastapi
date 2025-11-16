"""empty message

Revision ID: 150e90ebf24a
Revises: 4c54c47bbe28
Create Date: 2025-11-12 23:16:39.481496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '150e90ebf24a'
down_revision: Union[str, Sequence[str], None] = '4c54c47bbe28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
