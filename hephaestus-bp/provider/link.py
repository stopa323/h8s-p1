from model.link import LinkCreate, LinkObj, LinkPlugin


def create_link(link: LinkCreate, blueprint_id: str) -> LinkObj:
    _link = LinkPlugin.create(link, blueprint_id)
    return _link
