"""empty message

Revision ID: 79704841e691
Revises: 
Create Date: 2022-01-31 22:56:57.951516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79704841e691'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('working', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    op.create_table('works',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('work_name', sa.String(length=64), nullable=True),
    sa.Column('time_init', sa.DateTime(), nullable=False),
    sa.Column('time_final', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_works_work_name'), 'works', ['work_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_works_work_name'), table_name='works')
    op.drop_table('works')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###