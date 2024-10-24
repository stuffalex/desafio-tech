from alembic import op
import sqlalchemy as sa

revision = '202410241050'  # Update this to a unique ID
down_revision = '202310241050' # Set this to the previous revision ID, if any
branch_labels = None
depends_on = None

def upgrade():
    op.drop_table('clientes_fornecedores')
    op.drop_table('clientes')
    op.drop_table('fornecedores')

    # Create fornecedores table
    op.create_table(
        'fornecedores',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String, unique=True, nullable=False),
        sa.Column('logo', sa.String, nullable=False),
        sa.Column('custoKwh', sa.Numeric, nullable=False),
        sa.Column('limiteMinimoKwh', sa.Numeric, nullable=True),
        sa.Column('ufOrigem', sa.String, nullable=True),
    )

    # Create clientes table
    op.create_table(
        'clientes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String, nullable=True),
        sa.Column('kwhMensal', sa.Numeric, nullable=True),
        sa.Column('ufOrigem', sa.String, nullable=True),
    )

    # Create clientes_fornecedores table
    op.create_table(
        'clientes_fornecedores',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('rating', sa.Numeric, nullable=True),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey('clientes.id'), nullable=False),
        sa.Column('fornecedor_id', sa.Integer, sa.ForeignKey('fornecedores.id'), nullable=False),
    )

def downgrade():
    op.drop_table('clientes_fornecedores')
    op.drop_table('clientes')
    op.drop_table('fornecedores')
