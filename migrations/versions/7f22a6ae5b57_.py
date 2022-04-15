"""empty message

Revision ID: 7f22a6ae5b57
Revises: 80fc03cbea51
Create Date: 2022-04-15 00:55:15.980670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f22a6ae5b57'
down_revision = '80fc03cbea51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe_posts', sa.Column('image', sa.String(length=36), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe_posts', 'image')
    # ### end Alembic commands ###
