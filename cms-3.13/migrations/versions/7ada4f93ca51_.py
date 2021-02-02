"""empty message

Revision ID: 7ada4f93ca51
Revises: 
Create Date: 2019-02-26 20:28:15.838462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ada4f93ca51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'article_tag', 'jq_article', ['jq_article.aid'], ['aid'])
    op.create_foreign_key(None, 'article_tag', 'jq_tag', ['jq_tag.tid'], ['tid'])
    op.create_foreign_key(None, 'jq_adminlog', 'jq_user', ['admin_id'], ['uid'])
    op.add_column('jq_article', sa.Column('flag', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'jq_article', 'jq_user', ['author_id'], ['uid'])
    op.create_foreign_key(None, 'jq_article', 'jq_article_category', ['cat_id'], ['cat_id'])
    op.create_foreign_key(None, 'jq_oplog', 'jq_user', ['admin_id'], ['uid'])
    op.create_foreign_key(None, 'jq_user', 'jq_role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jq_user', type_='foreignkey')
    op.drop_constraint(None, 'jq_oplog', type_='foreignkey')
    op.drop_constraint(None, 'jq_article', type_='foreignkey')
    op.drop_constraint(None, 'jq_article', type_='foreignkey')
    op.drop_column('jq_article', 'flag')
    op.drop_constraint(None, 'jq_adminlog', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    # ### end Alembic commands ###
