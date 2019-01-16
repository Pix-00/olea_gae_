from .google_io import sheets
from .common import get_path, hyperlink, STATE_MAP, URL


def fy(projs):
    path = get_path('KP')
    k = sheets.count_rows(path) + 1
    path.col = 'A:K'
    path.row = f'{k}:{k+len(projs)}'
    rows = list()
    for proj in projs:
        rows.append([
            f"'{proj['ino']}", f"'{proj['title']}", f"'{proj.pid}", STATE_MAP[5], '0/0', '', '',
            f'=HYPERLINK("{URL}/es?i={proj.pid},FY,"&ROW(),"[人员]")',
            hyperlink(proj['ids.doc'], 'FY'), ''
        ])
    sheets.append(path, rows)
    return True

def kp(projs):
    path = get_path('KP')
    k = sheets.count_rows(path) + 1
    path.col = 'A:K'
    path.row = f'{k}:{k+len(projs)}'
    rows = list()
    for i, proj in enumerate(projs, k):
        rows.append([
            f"'{proj['ino']}", f"'{proj['title']}", f"'{proj.pid}", STATE_MAP[5], '0/0', '', '',
            f'=IF(D{i}="{STATE_MAP[5]}",HYPERLINK("{URL}/p?i={proj.pid},KP,"&ROW(),"[跳过]"),"")',
            f'=HYPERLINK("{URL}/es?i={proj.pid},KP,"&ROW(),"[人员]")',
            hyperlink(proj['ids.doc'], 'GG'),
            f'=IF(E{i}="0/0","",createD(C{i},ROW()))'
        ])
    sheets.append(path, rows)
    return True

def uj(proj):
    path = get_path('UJ')
    k = sheets.count_rows(path) + 1
    path.col = 'A:L'
    path.row = k
    row = [[
        f"'{proj['ino']}", f"'{proj['title']}", f"'{proj.pid}", STATE_MAP[5], '0/0', '', '',
        f'=IF(D{k}="{STATE_MAP[5]}",HYPERLINK("{URL}/p?i={proj.pid},UJ,"&ROW(),"[跳过]"),"")',
        f'=HYPERLINK("{URL}/es?i={proj.pid},UJ,"&ROW(),"[人员]")',
        hyperlink(proj['ids.doc'], 'GG'),
        hyperlink(proj['ids.ext'], 'KP'),
        f'=IF(E{k}="0/0","",createF(C{k},ROW()))'
    ]]
    sheets.append(path, row)
    return True

def py(proj):
    path = get_path('PY')
    k = sheets.count_rows(path) + 1
    path.col = 'A:K'
    path.row = k
    row = [[
        f"'{proj['ino']}", f"'{proj['title']}", f"'{proj.pid}", STATE_MAP[5], '0/0', '', '',
        f'=HYPERLINK("{URL}/es?i={proj.pid},PY,"&ROW(),"[人员]")',
        hyperlink(proj['ids.doc'], 'GG'),
        hyperlink(proj['ids.ext'], 'KP'),
        f'=IF(E{k}="0/0","",createF(C{k},ROW()))'
    ]]
    sheets.append(path, row)
    return True

def hq(proj, pic_url): # the url may not be the real url
    path = get_path('HQ')
    k = sheets.count_rows(path) + 1
    path.col = 'A:M'
    path.row = k
    row = [[
        f"'{proj['ino']}", f"'{proj['title']}", f"'{proj.pid}", STATE_MAP[5], '0/0', '', '',
        f'=HYPERLINK("{URL}/es?i={proj.pid},HQ,"&ROW(),"[人员]")',
        hyperlink(proj['ids.doc'], 'GG'),
        hyperlink(proj['ids.ext'], 'KP'),
        hyperlink(proj['ids.mic'], 'PY'),
        hyperlink(pic_url, 'UJ'),
        f'=IF(E{k}="0/0","",createF(C{k},ROW()))'
    ]]
    sheets.append(path, row)
    return True

def lb(proj_infos):
    path = get_path('LB')
    k = sheets.count_rows(path) + 1
    path.col = 'A:C'
    path.row = f'{k}:{k+len(proj_infos)}'
    rows = list()
    for pi in proj_infos:
        rows.append([f"'{pi[0]}", f"'{pi[1]}", f"'{pi[2]}", '初始', '', f'=HYPERLINK("{URL}/p?i={pi[2]},LB,"&ROW(),"[设定链接]")'])
    sheets.append(path, rows)
    return True
