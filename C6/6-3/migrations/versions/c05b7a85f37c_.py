"""empty message

Revision ID: c05b7a85f37c
Revises: 
Create Date: 2019-02-07 12:20:17.980784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c05b7a85f37c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('abstract', sa.String(length=200), nullable=True))
    op.add_column('news', sa.Column('tags', sa.String(length=320), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'tags')
    op.drop_column('news', 'abstract')
    # ### end Alembic commands ###
