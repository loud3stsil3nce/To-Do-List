"""tasks table

Revision ID: 97829415d064
Revises: 1f1a5fee2ff9
Create Date: 2025-03-10 02:36:28.904131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97829415d064'
down_revision = '1f1a5fee2ff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_timestamp'), 'task', ['timestamp'], unique=False)
    op.create_index(op.f('ix_task_user_id'), 'task', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_user_id'), table_name='task')
    op.drop_index(op.f('ix_task_timestamp'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###
