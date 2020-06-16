"""empty message

Revision ID: 6b4c71b2644b
Revises: 7f281f43220f
Create Date: 2020-06-16 15:52:54.767087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b4c71b2644b'
down_revision = '7f281f43220f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('movies_actor_id_fkey', 'movies', type_='foreignkey')
    op.create_foreign_key(None, 'movies', 'actors', ['actor_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movies', type_='foreignkey')
    op.create_foreign_key('movies_actor_id_fkey', 'movies', 'actors', ['actor_id'], ['id'])
    # ### end Alembic commands ###
