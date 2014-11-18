def damage_calc_witharmor(rangefire, gun, location):
    damage = gun.basedmg * gun.armorpen/2 * hitboxmodifier(location) * gun.rangemod**(rangefire/500.)
    return damage
    
def damage_calc_noarmor(rangefire, gun, location):
    damage = gun.basedmg * hitboxmodifier(location) * gun.rangemod**(rangefire/500.)
    return damage

    
def hitboxmodifier(location):
    if( location == 'head'):
        hitboxmod = 4.00
    if( location == 'chest'):
        hitboxmod = 1.00
    if( location == 'stomach'):
        hitboxmod = 1.25
    if( location == 'leg'):
        hitboxmod = 0.75    
    return hitboxmod
