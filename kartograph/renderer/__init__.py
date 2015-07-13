from __future__ import absolute_import


class MapRenderer(object):

    def __init__(self, map):
        self.map = map

    def render(self):
        pass

    def write(self, filename):
        raise NotImplementedError('Not implemented yet')

    def preview(self):
        raise NotImplementedError('Not implemented yet')


from .svg import SvgRenderer

__all__ = ['MapRenderer', 'SvgRenderer']
