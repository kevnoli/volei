"""empty message

Revision ID: 76045a68da77
Revises: 1d37db8f487c
Create Date: 2024-05-02 12:58:00.158493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '76045a68da77'
down_revision: Union[str, None] = '1d37db8f487c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
                    sa.Column('weekday', sa.Integer(), nullable=False),
                    sa.Column('start_date', sa.Time(timezone=True), nullable=False),
                    sa.Column('end_date', sa.Time(timezone=True), nullable=False),
                    sa.Column('voting_until', sa.Time(timezone=True), nullable=False),
                    sa.Column('checkin_from', sa.Time(timezone=True), nullable=False),
                    sa.Column('checkin_until', sa.Time(timezone=True), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    # ### end Alembic commands ###
