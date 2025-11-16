"""add phone

Revision ID: cfb710b9852c
Revises: c13eb1b445a9
Create Date: 2025-11-14 08:04:58.430000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfb710b9852c'
down_revision: Union[str, Sequence[str], None] = 'c13eb1b445a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
