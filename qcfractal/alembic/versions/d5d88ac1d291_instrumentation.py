"""Instrumentation column additions

Revision ID: d5d88ac1d291
Revises: 1bd2f7711e68
Create Date: 2019-10-29 16:51:08.635880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d88ac1d291'
down_revision = '1bd2f7711e68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server_stats_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('collection_count', sa.Integer(), nullable=True),
    sa.Column('molecule_count', sa.Integer(), nullable=True),
    sa.Column('result_count', sa.Integer(), nullable=True),
    sa.Column('kvstore_count', sa.Integer(), nullable=True),
    sa.Column('access_count', sa.Integer(), nullable=True),
    sa.Column('result_states', sa.JSON(), nullable=True),
    sa.Column('db_total_size', sa.BigInteger(), nullable=True),
    sa.Column('db_table_size', sa.BigInteger(), nullable=True),
    sa.Column('db_index_size', sa.BigInteger(), nullable=True),
    sa.Column('db_table_information', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_server_stats_log_timestamp', 'server_stats_log', ['timestamp'], unique=False)
    op.create_table('queue_manager_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manager_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('completed', sa.Integer(), nullable=True),
    sa.Column('submitted', sa.Integer(), nullable=True),
    sa.Column('failures', sa.Integer(), nullable=True),
    sa.Column('total_worker_walltime', sa.Float(), nullable=True),
    sa.Column('total_task_walltime', sa.Float(), nullable=True),
    sa.Column('active_tasks', sa.Integer(), nullable=True),
    sa.Column('active_cores', sa.Integer(), nullable=True),
    sa.Column('active_memory', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['queue_manager.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_queue_manager_log_timestamp', 'queue_manager_logs', ['timestamp'], unique=False)
    op.add_column('queue_manager', sa.Column('active_cores', sa.Integer(), nullable=True))
    op.add_column('queue_manager', sa.Column('active_memory', sa.Float(), nullable=True))
    op.add_column('queue_manager', sa.Column('active_tasks', sa.Integer(), nullable=True))
    op.add_column('queue_manager', sa.Column('configuration', sa.JSON(), nullable=True))
    op.add_column('queue_manager', sa.Column('total_task_walltime', sa.Float(), nullable=True))
    op.add_column('queue_manager', sa.Column('total_worker_walltime', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('queue_manager', 'total_worker_walltime')
    op.drop_column('queue_manager', 'total_task_walltime')
    op.drop_column('queue_manager', 'configuration')
    op.drop_column('queue_manager', 'active_tasks')
    op.drop_column('queue_manager', 'active_memory')
    op.drop_column('queue_manager', 'active_cores')
    op.drop_index('ix_queue_manager_log_timestamp', table_name='queue_manager_logs')
    op.drop_table('queue_manager_logs')
    op.drop_index('ix_server_stats_log_timestamp', table_name='server_stats_log')
    op.drop_table('server_stats_log')
    # ### end Alembic commands ###
