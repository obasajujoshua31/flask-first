"""empty message

Revision ID: 15de73ad8ef8
Revises: 
Create Date: 2019-09-11 19:05:03.799629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15de73ad8ef8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bucket_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bucket_list')
    # ### end Alembic commands ###
