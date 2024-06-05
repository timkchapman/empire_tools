from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

class ForcesForm(FlaskForm):
    force = SelectField('Select Force', validators=[DataRequired()])
    quality = StringField('Force Quality', validators=[DataRequired()])
    order = SelectField('Order', validators=[DataRequired()])
    ritual = SelectField('Ritual', validators=[DataRequired()])
    strength = StringField('Enter Strength', validators=[DataRequired(), Length(min=1, max=4)])

class FortificationsForm(FlaskForm):
    fortification = SelectField('Select Force', validators=[DataRequired()])
    ritual = SelectField('Ritual', validators=[DataRequired()])
    fortification_is_besieged = BooleanField('Fort is Besieged?', validators=[DataRequired()])
    strength = StringField('Enter Strength', validators=[DataRequired(), Length(min=1, max=4)])

class MilitaryUnitsForm(FlaskForm):
    military_units = StringField('Military Units', validators=[DataRequired()])
    supported_force = SelectField('Supported Army', validators=[DataRequired()])