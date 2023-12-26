from sharp_stone import SharpStone
CRAFTS_MAP = {
    ("stone", "stone"): (None, "sharp_stone"),
    ("sharp_stone", "tree"): ("sharp_stone", "brevno"),
    ("sharp_stone", "paporotnic"): ("sharp_stone", "thread")

}  # сдесь записываются крафты в формате [entity_name, entity_name]: entity
