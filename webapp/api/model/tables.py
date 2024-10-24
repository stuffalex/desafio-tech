from api import db


class Fornecedor(db.Model):
    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    logo = db.Column(db.String)
    custoKwh = db.Column(db.Numeric)
    limiteMinimoKwh = db.Column(db.Numeric)
    ufOrigem = db.Column(db.String)

    def __init__(self,nome, logo, custoKwh, limiteMinimoKwh, ufOrigem):
        self.nome = nome
        self.logo = logo
        self.custoKwh = custoKwh
        self.limiteMinimoKwh = limiteMinimoKwh
        self.ufOrigem = ufOrigem

    def __repr__(self):
        return "<Fornecedor %r>" % self.nome

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    kwhMensal = db.Column(db.Numeric)
    ufOrigem = db.Column(db.String)

    def __init__(self,nome, kwhMensal, ufOrigem):
        self.nome = nome
        self.kwhMensal = kwhMensal
        self.ufOrigem = ufOrigem

    def __repr__(self):
        return "<Cliente %r>" % self.nome

class ClienteFornecedor(db.Model):
    __tablename__ = "clientes_fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Numeric)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))

    cliente = db.relationship('Cliente', foreign_keys=cliente_id)
    fornecedor = db.relationship('Fornecedor', foreign_keys=fornecedor_id)

    def __init__(self, rating, cliente_id, fornecedor_id):
        self.rating = rating
        self.cliente_id = cliente_id
        self.fornecedor_id = fornecedor_id

    def __repr__(self):
        return "<ClienteFornecedor %r>" % self.id  % self.fornecedor_id