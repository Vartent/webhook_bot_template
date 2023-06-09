"""create user table

Revision ID: 450df09e5038
Revises: 
Create Date: 2023-04-30 15:09:54.112420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450df09e5038'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
