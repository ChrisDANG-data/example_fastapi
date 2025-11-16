"""add phone number in users

Revision ID: e1624eb08147
Revises: 1faaf4f54074
Create Date: 2025-11-13 13:37:28.236870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1624eb08147'
down_revision: Union[str, Sequence[str], None] = '1faaf4f54074'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
