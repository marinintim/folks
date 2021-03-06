"""3

Revision ID: d8472e568126
Revises: 8d11fb6238b0
Create Date: 2019-08-18 09:44:15.108422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8472e568126'
down_revision = '8d11fb6238b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flags',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flags')
    # ### end Alembic commands ###
