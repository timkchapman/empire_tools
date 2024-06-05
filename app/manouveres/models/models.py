from app import db

class Force(db.Model):
    force_id = db.Column(db.Integer, primary_key=True, index=True)
    force_name = db.Column(db.String(80), unique=True, nullable=False)
    force_is_army = db.Column(db.Boolean, nullable=False)
    nation_id = db.Column(db.Integer, db.ForeignKey('nation.nation_id'), nullable=False)
    quality_id = db.Column(db.Integer, db.ForeignKey('quality.quality_id'), nullable=False)
    large = db.Column(db.Boolean, nullable=False)

    nation = db.relationship('Nation', lazy='joined')
    quality = db.relationship('Quality', lazy='joined')

    def __repr__(self):
        return '<Force %r>' % self.force_name
    
class Fortification(db.Model):
    fortification_id = db.Column(db.Integer, primary_key=True, index=True)
    fortification_name = db.Column(db.String(80), unique=True, nullable=False)
    fortification_level = db.Column(db.Integer, nullable=False)
    fortification_maximum_strength = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Fortification %r>' % self.fortification_name
    
class Nation(db.Model):
    nation_id = db.Column(db.Integer, primary_key=True, index=True)
    nation_name = db.Column(db.String(80), unique=True, nullable=False)
    nation_faction = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Nation %r>' % self.nation_name
    
quality_order_association = db.Table('quality_order',
    db.Column('quality_id', db.Integer, db.ForeignKey('quality.quality_id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True)
)

class Quality(db.Model):
    quality_id = db.Column(db.Integer, primary_key=True, index=True)
    quality_name = db.Column(db.String(80), unique=True, nullable=False)
    quality_effects = db.Column(db.Text, nullable=False)
    quality_descriptors = db.Column(db.Text, nullable=False)
    quality_description = db.Column(db.Text, nullable=False)
    quality_orders = db.relationship('Order', secondary=quality_order_association,  lazy='subquery',
                             backref=db.backref('qualities', lazy=True))

    def __repr__(self):
        return '<Quality %r>' % self.quality_name
    
    def effects_as_list(self):
        return self.quality_effects.split('. ')

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, index=True)
    order_name = db.Column(db.String(80), unique=True, nullable=False)
    offensive_order = db.Column(db.Boolean, nullable=False)
    order_effects = db.Column(db.Text, nullable=False)
    order_description = db.Column(db.Text(80), nullable=False)
    casualties_inflicted_modifier = db.Column(db.Float, nullable=False)
    casualties_suffered_modifier = db.Column(db.Float, nullable=False)
    territory_claimed_modifier = db.Column(db.Float, nullable=False)
    territory_defence_modifier = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.order_name
    
    def effects_as_list(self):
        return self.order_effects.split('. ')

class Force_Ritual(db.Model):
    force_ritual_id = db.Column(db.Integer, primary_key=True, index=True)
    force_ritual_name = db.Column(db.String(80), unique=True, nullable=False)
    army_ritual = db.Column(db.Boolean, nullable=False)
    force_ritual_effects = db.Column(db.Text, nullable=False)
    force_ritual_quality_id = db.Column(db.Integer, db.ForeignKey('quality.quality_id'), nullable=True)
    force_effective_strength_modifier = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Force_Ritual %r>' % self.force_ritual_name

class Fortification_Ritual(db.Model):
    fortification_ritual_id = db.Column(db.Integer, primary_key=True, index=True)
    fortification_ritual_name = db.Column(db.String(80), unique=True, nullable=False)
    fortification_ritual_effects = db.Column(db.Text, nullable=False)
    fortification_effective_strength_modifier = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Fortification_Ritual %r>' % self.fortification_ritual_name

class Territory_Ritual(db.Model):
    territory_ritual_id = db.Column(db.Integer, primary_key=True, index=True)
    territory_ritual_name = db.Column(db.String(80), unique=True, nullable=False)
    territory_ritual_effects = db.Column(db.Text, nullable=False)
    territory_ritual_casualties = db.Column(db.Integer, nullable=False)
    territory_ritual_modifier = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Territory_Ritual %r>' % self.territory_ritual_name