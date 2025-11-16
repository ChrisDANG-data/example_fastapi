"""drop users

Revision ID: c13eb1b445a9
Revises: 1c6a3f607b79
Create Date: 2025-11-14 08:00:01.185559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c13eb1b445a9'
down_revision: Union[str, Sequence[str], None] = '1c6a3f607b79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
