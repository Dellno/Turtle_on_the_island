# все крафты игры
CRAFTS_MAP = {
    # (предмет в инвенторе, предмет рядом):(предмет в инвенторе, новый предмет рядом)
    ("stone", "stone"): ("sharp_stone", "stone", None),
    ('topor', "tree"): ('topor', "brevno", None),
    ("sharp_stone", "paporotnic"): ("sharp_stone", "thread", None),
    ("sharp_stone", "dry_bush"): ("sharp_stone", 'stick', None),
    ('brevno', 'brevno'): (None, 'brevno_2', None),
    ('brevno', 'brevno_2'): (None, 'brevno_3', None),
    ('brevno', 'brevno_3'): (None, 'brevno_4', None),
    ('thread', 'brevno_4'): (None, 'plot', None),
    (None, 'brevno_2'): ('brevno', 'brevno', None),
    (None, 'brevno_3'): ('brevno', 'brevno_2', None),
    (None, 'brevno_4'): ('brevno', 'brevno_3', None),
    (None, "endurance_crystal"): (None, None, "endurance_crystal"),
    (None, "health_cristal"): (None, None, "health_cristal"),
    ('stick', "sharp_stone"): ('topor', None, None),

    ('brevno_2', 'ship_1'): (None, 'ship_13', 'fixed_ship'),
    ('brevno_2', 'ship_2'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_4'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_5'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_6'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_7'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_8'): (None, 'ship_20', 'fixed_ship'),
    ('brevno_2', 'ship_9'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_10'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_11'): (None, None, 'fixed_ship'),
    ('brevno_2', 'ship_12'): (None, None, 'fixed_ship'),

}
