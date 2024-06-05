def convert_to_rings(rings=0, crowns=0, thrones=0):
    total_rings = rings + crowns * 20 + thrones * 160
    return total_rings

def convert_from_rings(rings, output_unit):
    if output_unit == "rings":
        return {'rings': rings}
    elif output_unit == "crowns":
        crowns = rings // 20
        remaining_rings = rings % 20
        return {'crowns': crowns, 'rings': remaining_rings}
    elif output_unit == "thrones":
        thrones = rings // 160
        remaining_rings = rings % 160
        crowns = remaining_rings // 20
        rings = remaining_rings % 20
        return {'thrones': thrones, 'crowns': crowns, 'rings': rings}
    else:
        raise ValueError("Invalid output unit")