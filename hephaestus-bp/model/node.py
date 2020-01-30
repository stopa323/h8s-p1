import uuid
from enum import Enum
from typing import Type, Union

from common.db import get_client
from schema.base import HasId


db = get_client()


class HNodeKind(Enum):
    BP_INGRESS = "H.BPIngress"
    BP_EGRESS = "H.BPEgress"


class NodeDB(HasId):
    kind: str
    name: str
    blueprint_id: uuid.UUID


class BPIngressNodeDB(NodeDB):
    name: str = "Blueprint Ingress"
    kind: str = HNodeKind.BP_INGRESS.value


class BPEgressNodeDB(NodeDB):
    name: str = "Blueprint Egress"
    kind: str = HNodeKind.BP_EGRESS.value


class NodeDBPlugin:

    @classmethod
    def get_model(cls, kind: HNodeKind) -> Union[
        Type[BPIngressNodeDB],
        Type[BPEgressNodeDB]]:
        try:
            model = {
                HNodeKind.BP_INGRESS: BPIngressNodeDB,
                HNodeKind.BP_EGRESS: BPEgressNodeDB
            }[kind]

            return model
        except KeyError:
            raise ValueError(f"Unknown node kind: {kind.value}")

    @classmethod
    def create(cls, kind: HNodeKind, bp_id: str) -> NodeDB:
        model = cls.get_model(kind)

        data = {"blueprint_id": bp_id, "id": uuid.uuid4()}

        node = model(**data)
        data = node.dict()
        data["_id"] = data["id"]
        del data["id"]
        db.nodes.insert_one(data)

        return model(**data)
