"""empty message

Revision ID: b4f094d9587f
Revises: 5454e9ab0750
Create Date: 2018-12-07 20:40:10.516009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4f094d9587f'
down_revision = '5454e9ab0750'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jq_article_category',
    sa.Column('cat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('cat_name', sa.String(length=20), nullable=False),
    sa.Column('keywords', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('cat_sort', sa.Integer(), nullable=True),
    sa.Column('template', sa.String(length=80), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('dir', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('cat_id')
    )
    op.create_table('jq_article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=False),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('list_image_url', sa.String(length=256), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['jq_user.uid'], ),
    sa.ForeignKeyConstraint(['cat_id'], ['jq_article_category.cat_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'jq_user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jq_user', type_='unique')
    op.drop_table('jq_article')
    op.drop_table('jq_article_category')
    # ### end Alembic commands ###
