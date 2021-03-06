"""empty message

Revision ID: 17e6c4de9562
Revises: 328bf1c6d743
Create Date: 2018-11-25 13:48:47.439216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17e6c4de9562'
down_revision = '328bf1c6d743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jq_user', sa.Column('password', sa.String(length=100), nullable=False))
    op.drop_index('email', table_name='jq_user')
    op.drop_column('jq_user', 'reg_time')
    op.drop_column('jq_user', '_password')
    op.drop_column('jq_user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jq_user', sa.Column('email', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('jq_user', sa.Column('_password', mysql.VARCHAR(length=100), nullable=False))
    op.add_column('jq_user', sa.Column('reg_time', mysql.DATETIME(), nullable=True))
    op.create_index('email', 'jq_user', ['email'], unique=True)
    op.drop_column('jq_user', 'password')
    # ### end Alembic commands ###
