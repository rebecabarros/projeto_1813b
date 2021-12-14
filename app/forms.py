from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, URL 

class ContatoForm(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    mensagem = TextAreaField("Mensagem: ", validators=[DataRequired()])
    submit = SubmitField("Enviar")

class GravadoraForm (FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()])
    endereco = StringField('Endereço: ')
    telefone = StringField('Telefone: ')
    site = StringField('Site: ', validators=[URL()])
    contato = StringField('Contato: ')
    submit = SubmitField('Salvar')
