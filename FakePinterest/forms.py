# Criar formularios do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, length, ValidationError
from FakePinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente! crie uma conta")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    username = StringField("Nome do usuário:", validators=[DataRequired()])
    senha = PasswordField("Senha:", validators=[DataRequired(), length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação da Senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado faça o login para continuar!")


class FormFotos(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")