"""empty message

Revision ID: 328bf1c6d743
Revises: a1cc8d7b9cb9
Create Date: 2018-11-25 11:33:13.921368

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '328bf1c6d743'
down_revision = 'a1cc8d7b9cb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jq_user', sa.Column('_password', sa.String(length=100), nullable=False))
    op.drop_column('jq_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jq_user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('jq_user', '_password')
    # ### end Alembic commands ###
