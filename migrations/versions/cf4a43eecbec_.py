"""empty message

Revision ID: cf4a43eecbec
Revises: 2a34f5632a04
Create Date: 2023-09-03 13:43:19.992187

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf4a43eecbec'
down_revision = '2a34f5632a04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('xxx',
    sa.Column('number', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('verification', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('number')
    )
    op.drop_table('email_verification')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_verification',
    sa.Column('number', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('verification', mysql.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('number'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('xxx')
    # ### end Alembic commands ###
