"""Update Blog Model Migration

Revision ID: 4e7966835551
Revises: a855999bce36
Create Date: 2022-05-20 23:23:37.218185

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4e7966835551'
down_revision = 'a855999bce36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogPosts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_pic_path', sa.String(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('postedDate', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('blogs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('blog_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('postedDate', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='blogs_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blogs_pkey')
    )
    op.drop_table('blogPosts')
    # ### end Alembic commands ###
