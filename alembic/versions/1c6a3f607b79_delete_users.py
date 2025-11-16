"""delete users

Revision ID: 1c6a3f607b79
Revises: e1624eb08147
Create Date: 2025-11-13 23:37:29.588103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c6a3f607b79'
down_revision: Union[str, Sequence[str], None] = 'e1624eb08147'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
