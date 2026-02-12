from collections import defaultdict
from typing import Tuple

from docutils.nodes import Element
from sphinx.addnodes import desc_name, desc_signature
from sphinx.directives import ObjectDescription
from sphinx.domains import Index
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole

NORMAL_ENTRY = 0


class ZenTypeDirective(ObjectDescription):
    def handle_signature(self, sig: str, signode: desc_signature):
        signode += desc_name(text=sig)
        return sig

    def add_target_and_index(self, name, sig: str, signode: desc_signature):
        signode['ids'].append('zentype-' + sig)
        self.env.get_domain(self.domain).add_type(sig)  # type: ignore


class ZenTypeIndex(Index):
    name = 'zentype'
    localname = 'ZenType Index'
    shortname = 'ZenType'

    def generate(self, docnames=None):
        content = defaultdict(list)

        # types in alphabetical order of simple names
        types = sorted(self.domain.get_objects(), key=lambda type: type[1])

        # Group by first letter of simple names
        for full_name, simple_name, _, docname, anchor, _ in types:
            content[simple_name[0].lower()].append(
                # name, subtype, docname, anchor, extra, qualifier, description
                (simple_name, NORMAL_ENTRY, docname, anchor, full_name, '', '')
            )

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())
        return content, True


class ZenTypeXRefRole(XRefRole):
    def process_link(self, env: "BuildEnvironment", refnode: Element,
                     has_explicit_title: bool, title: str, target: str
                     ) -> Tuple[str, str]:

        if not has_explicit_title:
            [*_, title] = title.split('.')
        return super().process_link(
            env, refnode, has_explicit_title, title, target)
