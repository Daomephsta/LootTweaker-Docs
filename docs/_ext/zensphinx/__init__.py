from collections import defaultdict
from typing import Iterable, Optional, Tuple

import sphinx.util.nodes as sphinx_nodes
from docutils.nodes import Element, reference
from sphinx.addnodes import pending_xref
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.domains import Domain
from sphinx.environment import BuildEnvironment
from sphinx.util import logging

from zensphinx.zenfunction import ZenFunctionDirective
from zensphinx.zentype import ZenTypeDirective, ZenTypeIndex, ZenTypeXRefRole

LOGGER = logging.getLogger(__name__)
PRIORITY_IMPORTANT = 1


class ZenSphinxDomain(Domain):
    name = 'zenscript'
    label = 'ZenScript extensions'
    roles = {
        'ref': ZenTypeXRefRole()
    }
    directives = {
        'type': ZenTypeDirective,
        'function': ZenFunctionDirective
    }
    indices = [
        ZenTypeIndex
    ]
    initial_data = {
        'types_by_name': {},
        'types_by_simple_name': defaultdict(set)
    }

    def add_type(self, full_name: str):
        [*_, simple_name] = full_name.split('.')
        anchor = 'zentype-' + full_name
        type = (full_name, simple_name, 'ZenType',
                self.env.docname, anchor, PRIORITY_IMPORTANT)
        self.data['types_by_name'][full_name] = type
        self.data['types_by_simple_name'][simple_name].add(type)

    def get_objects(self) -> Iterable[Tuple[str, str, str, str, str, int]]:
        return self.data['types_by_name'].values()

    def resolve_xref(self, env: 'BuildEnvironment', fromdocname: str,
                     builder: 'Builder', typ: str, target: str,
                     node: pending_xref, contnode: Element
                     ) -> None | reference:
        if '.' not in target:
            matches: set = self.data['types_by_simple_name'][target]
            if not matches:
                match = None
            elif len(matches) > 1:
                LOGGER.warning(f'{fromdocname}: Multiple types named {target}.'
                               ' Fully qualify the reference')
                return None
            else:
                [match] = matches
        else:
            match = self.data['types_by_name'].get(target)
        if match:
            _, _, _, to_docname, match_target, _ = match
            return sphinx_nodes.make_refnode(
                builder, fromdocname, to_docname,
                match_target, contnode, match_target)
        else:
            LOGGER.warning(f'Could not resolve {target}', location=node.source)
            return None

    def get_full_qualified_name(self, node: Element) -> Optional[str]:
        return 'zensphinx.' + node.arguments[0]  # type: ignore


def setup(app: Sphinx):
    app.add_domain(ZenSphinxDomain)
