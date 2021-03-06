"""empty message

Revision ID: 960a2a34b232
Revises: 9545b4d29405
Create Date: 2018-12-17 20:14:44.334636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960a2a34b232'
down_revision = '9545b4d29405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'article_tag', 'jq_tag', ['jq_tag.tid'], ['tid'])
    op.create_foreign_key(None, 'article_tag', 'jq_article', ['jq_article.aid'], ['aid'])
    op.create_foreign_key(None, 'jq_article', 'jq_user', ['author_id'], ['uid'])
    op.create_foreign_key(None, 'jq_article', 'jq_article_category', ['cat_id'], ['cat_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jq_article', type_='foreignkey')
    op.drop_constraint(None, 'jq_article', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    # ### end Alembic commands ###
