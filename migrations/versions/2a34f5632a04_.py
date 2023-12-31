"""empty message

Revision ID: 2a34f5632a04
Revises: 37ce0f7e8e88
Create Date: 2023-09-03 13:39:57.272465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2a34f5632a04'
down_revision = '37ce0f7e8e88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_verification', schema=None) as batch_op:
        batch_op.alter_column('number',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_verification', schema=None) as batch_op:
        batch_op.alter_column('number',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
