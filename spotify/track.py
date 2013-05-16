from __future__ import unicode_literals

from spotify import ffi, lib
from spotify.utils import to_bytes


__all__ = [
    'LocalTrack',
    'Track',
]


class Track(object):
    def __init__(self, sp_track, add_ref=True):
        if add_ref:
            lib.sp_track_add_ref(sp_track)
        self.sp_track = ffi.gc(sp_track, lib.sp_track_release)

    def as_link(self, offset=0):
        from spotify.link import Link
        return Link(self, offset=offset)

    # TODO Add sp_track_* methods


class LocalTrack(Track):
    def __init__(self, artist=None, title=None, album=None, length=None):
        if artist is not None:
            artist = ffi.new('char[]', to_bytes(artist))
        else:
            artist = ffi.NULL

        if title is not None:
            title = ffi.new('char[]', to_bytes(title))
        else:
            title = ffi.NULL

        if album is not None:
            album = ffi.new('char[]', to_bytes(album))
        else:
            album = ffi.NULL

        if album is None:
            album = -1

        sp_track = lib.sp_localtrack_create(artist, title, album, length)

        super(LocalTrack, self).__init__(sp_track, add_ref=False)
