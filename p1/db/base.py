import mongoengine as me

from uuid import uuid4


class DocumentId(me.Document):
    id = me.StringField(primary_key=True, required=True,
                        default=lambda: str(uuid4()))

    meta = {"allow_inheritance": True}


class EmbeddedDocumentId(me.Document):
    id = me.StringField(primary_key=True, required=True,
                        default=lambda: str(uuid4()))

    meta = {"allow_inheritance": True}
