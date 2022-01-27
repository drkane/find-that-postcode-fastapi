"""Add hash to postcode

Revision ID: 856755dc8521
Revises: a0863ceb4005
Create Date: 2022-01-27 11:56:21.933324

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "856755dc8521"
down_revision = "a0863ceb4005"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("postcodes", sa.Column("hash", sa.String(length=32), nullable=True))
    op.create_index(op.f("ix_postcodes_hash"), "postcodes", ["hash"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_postcodes_hash"), table_name="postcodes")
    op.drop_column("postcodes", "hash")
    # ### end Alembic commands ###