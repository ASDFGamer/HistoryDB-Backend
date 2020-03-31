from swagger_server.__main__ import db
from swagger_server.constants import NAME_MAX_LENGHT


class LanguageCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Use the ISO 639‑3 standard.
    code = db.Column(db.String(3), nullable=False)


class TypeEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_name = db.Column(db.String(NAME_MAX_LENGHT), nullable=False)
    default_language = db.Column(db.Integer, db.ForeignKey(LanguageCode.id), nullable=False)
    default_language_code = db.relationship(LanguageCode)


class TypeEventTranslation(db.Model):
    typeEvent_id = db.Column(db.Integer, db.ForeignKey(TypeEvent.id), primary_key=True)
    language_code = db.Column(db.Integer, db.ForeignKey(LanguageCode.id), primary_key=True)
    name = db.Column(db.String(NAME_MAX_LENGHT), nullable=False)
