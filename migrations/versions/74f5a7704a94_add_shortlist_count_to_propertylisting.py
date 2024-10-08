"""Add shortlist_count to PropertyListing

Revision ID: 74f5a7704a94
Revises: af7cf425d658
Create Date: 2024-05-17 20:20:10.536236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f5a7704a94'
down_revision = 'af7cf425d658'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertyListing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shortlist_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertyListing', schema=None) as batch_op:
        batch_op.drop_column('shortlist_count')

    # ### end Alembic commands ###
