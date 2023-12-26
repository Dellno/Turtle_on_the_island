from sharp_stone import SharpStone
CRAFTS_MAP = {
    ("stone", "stone"): (None, "sharp_stone"),
    ('sharp_stone', 'tree'): ('brevno', None),
    (None, 'paporotnik'): ('thread', None),
    (None, 'tree'): ('tree', 'stick'),
    ('brevno', 'brevno', 'brevno', 'thread', 'thread'): ('plot')
}  # сдесь записываются крафты в формате [entity_name, entity_name]: entity
