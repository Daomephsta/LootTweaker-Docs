import re
from typing import Any, Callable, List

from docutils import nodes
from docutils.nodes import Node, Text, reference
from docutils.parsers.rst import directives
from sphinx.addnodes import desc_signature, pending_xref
from sphinx.directives import ObjectDescription

ANNOTATION = re.compile(r'@\w+\s*')


def multi(
          suboptions: List[Callable[[str], Any]]
         ) -> Callable[[str], List[Any]]:
    return lambda str: [suboption(raw) for suboption, raw in
                        zip(suboptions, str.split(' '))]


class ZenFunctionDirective(ObjectDescription):
    option_spec = {
        'noindex': directives.flag,
        'external-type': multi([str, directives.uri])
    }

    def link_type(self, type_name: str) -> List[nodes.Node]:
        link = []
        array_brackets = type_name.find('[')
        if array_brackets != -1:
            link.append(Text(type_name[array_brackets:]))
            type_name = type_name[:array_brackets]
        ext_type_0 = self.options['external-type'][0]
        if 'external-type' in self.options and ext_type_0 == type_name:
            link.insert(0, reference('', Text(type_name),
                                     refuri=self.options['external-type'][1]))
        else:
            link.insert(0, pending_xref(
                '', Text(type_name), refdomain=self.domain,
                reftype='zentype', reftarget=type_name))
        return link

    def parse_signature(self, signature: str
                        ) -> tuple[bool, str, str, list[tuple[str, str]]]:

        args_start = signature.find('(')
        match signature[:args_start].split(' ', maxsplit=2):
            case ['static', return_type, name]:
                static = True
            case ['static', name]:
                static = True
                return_type = ''
            case [return_type, name]:
                static = False
            case [name]:
                static = False
                return_type = ''
            case _:
                raise ValueError('Could not parse ' + signature)

        # Isolate parameter list
        parameters: list[tuple[str, str]]
        parameters_temp = signature[args_start + 1:-1]
        if parameters_temp:
            # Strip annotations
            parameters_temp = ANNOTATION.sub('', parameters_temp)
            # Split into individual parameters
            parameters_temp = parameters_temp.split(',')
            # Map parameters into name-type pairs
            parameters = [tuple(p.strip().split(' '))  # type: ignore
                          for p in parameters_temp]
        else:
            parameters = []
        return static, return_type, name, parameters

    def handle_parameter(self, p_type: str, p_name: str) -> List[Node]:
        return self.link_type(p_type) + [Text(' ' + p_name)]

    def handle_signature(self, sig: str, signode: desc_signature) -> str:
        static, return_type, name, parameters = self.parse_signature(sig)
        if static:
            signode += Text('static ')
        if return_type:
            signode += self.link_type(return_type)
        signode += Text(f' {name}(')
        for parameter in parameters:
            signode += self.handle_parameter(*parameter)
            if parameter != parameters[-1]:
                signode += Text(', ')
        signode += Text(') ')
        parameter_types = '-'.join([type for type, _ in parameters])
        return f'zenfunction-{name}({parameter_types})'

    def add_target_and_index(self, name: str, sig: str,
                             signode: desc_signature):
        signode['ids'].append(name)
