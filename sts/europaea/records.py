import time

from . import sheets
from .common import get_path, hyperlink


HL_COL_MAP = {
    'KP': 'K',
    'SJ': 'K',
    'PY': 'K',
    'HQ': 'K'}

def set_hyperlink(sc, row, id_):
    path = get_path(sc)
    path.col = HL_COL_MAP[sc]
    path.row = row
    sheets.set_values(path, [[hyperlink(id_, sc)]])
    return True

class LbLineCache:
    cache = dict()
    time = 0

    @classmethod
    def update(cls):
        now = time.time()
        if now - cls.time > 120:
            cls.cache.clear()
            path = get_path('LB')
            path.col = 'C'
            path.row = '2:'
            for k, line in enumerate(sheets.get_values(path), 2):
                cls.cache[line[0]] = k

def get_LB_line(pid):
    LbLineCache.update()
    return LbLineCache.cache[pid]

def update_process_info(proj):
    path = get_path('LB')
    path.col = 'B:C'
    path.row = get_LB_line(proj.pid)
    sheets.set_values(path, [[proj.ssc_display, proj.all_staff]])
    return True
