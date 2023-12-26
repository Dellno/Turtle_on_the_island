from sharp_stone import SharpStone
CRAFTS_MAP = {
    # (предмет в инвенторе, предмет рядом):(предмет в инвенторе, новый предмет рядом)
    ("stone", "stone"): (None, "sharp_stone"),
    ("sharp_stone", "tree"): ("sharp_stone", "brevno"),
    ("sharp_stone", "paporotnic"): ("sharp_stone", "thread"),
    (None, 'tree'): ('stick', 'tree'),
    ('brevno', 'brevno'): (None, 'brevno_2'),
    ('brevno', 'brevno_2'): (None, 'brevno_3'),
    ('brevno', 'brevno_3'): (None, 'brevno_4'),
    ('thread', 'brevno_4'): (None, 'plot'),
    (None, 'brevno_2'): ('brevno', 'brevno'),
    (None, 'brevno_3'): ('brevno', 'brevno_2'),
    (None, 'brevno_4'): ('brevno', 'brevno_3')

}  # сдесь записываются крафты в формате [entity_name, entity_name]: entity
