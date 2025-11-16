"""create new user

Revision ID: 617b0555e7b7
Revises: cfb710b9852c
Create Date: 2025-11-14 08:08:47.209775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '617b0555e7b7'
down_revision: Union[str, Sequence[str], None] = 'cfb710b9852c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("new_users",sa.Column("id",sa.Integer, primary_key=True, nullable=False),
                    sa.Column("email",sa.String,nullable=False, unique=True),
                    sa.Column("password",sa.String, nullable=False),
                    sa.Column("createdon",sa.TIMESTAMP(timezone=True),server_default=sa.text("NOW()")),
                    sa.Column("telephone",sa.String, nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    
   
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("new_users")
    pass
