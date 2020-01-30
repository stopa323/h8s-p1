from typing import List

from common.db import get_client


db = get_client()


def get_molds() -> List[str]:
    return ['a']
