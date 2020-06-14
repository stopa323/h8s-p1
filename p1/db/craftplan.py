import mongoengine as me

from p1.db.base import DocumentId, EmbeddedDocumentId


class PortObj(EmbeddedDocumentId):
    name = me.StringField()
    kind = me.StringField()
    value = me.StringField()


class NodeObj(EmbeddedDocumentId):
    kind = me.StringField()
    automoton = me.StringField()
    ingress_ports = me.ListField(PortObj)
    egress_ports = me.ListField(PortObj)


class CraftPlanObj(DocumentId):
    name = me.StringField()
    description = me.StringField()
    nodes = me.ListField(NodeObj)
