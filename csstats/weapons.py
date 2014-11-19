#!/usr/bin/env python

import csv


STATS = """Type,WeaponArmorRatio,Damage,RangeModifier,CycleTime,Penetration,KillAward,MaxPlayerSpeed,clip_size,WeaponPrice,Range,FullAuto,Bullets,TracerFrequency,FlinchVelocityModifierLarge
pistol,deagle,1.864,63,0.810,0.225,2,$300,230,7,$800,4096,0,1,1,0.55
pistol,elites,1.050,38,0.750,0.120,1,$300,240,30,$500,4096,0,1,0,0.55
pistol,fiveseven,1.823,32,0.810,0.150,1,$300,240,20,$500,4096,0,1,1,0.55
pistol,glock,0.940,28,0.900,0.150,1,$300,240,20,$200,4096,0,1,1,0.55
pistol,hkp2000,1.010,35,0.910,0.170,1,$300,240,13,$200,4096,0,1,1,0.55
pistol,usp_silencer,1.010,35,0.910,0.170,1,$300,240,12,$200,4096,0,1,1,0.55
pistol,p250,1.553,35,0.850,0.150,1,$300,240,13,$300,4096,0,1,1,0.55
pistol,cz75a,1.553,35,0.850,0.100,1,$300,240,12,$500,4096,1,1,1,0.55
pistol,tec9,1.812,33,0.831,0.120,1,$300,240,32,$500,4096,0,1,1,0.55
pistol,mag7,1.500,30,0.450,0.850,1,$900,225,5,$1800,1400,1,8,1,0.35
shotgun,nova,1.000,26,0.700,0.880,0,$900,220,8,$1200,3000,1,9,1,0.35
shotgun,sawedoff,1.500,32,0.450,0.850,1,$900,210,7,$1200,650,0,8,1,0.35
shotgun,xm1014,1.600,20,0.700,0.350,1,$900,215,7,$2000,3000,1,6,1,0.35
smg,bizon,1.150,27,0.800,0.080,1,$600,240,64,$1400,3600,1,1,3,0.55
smg,mac10,1.150,29,0.800,0.075,1,$600,240,30,$1050,3600,1,1,3,0.55
smg,mp7,1.250,29,0.850,0.080,1,$600,220,30,$1700,3600,1,1,3,0.55
smg,mp9,1.200,26,0.830,0.070,1,$600,240,30,$1250,3600,1,1,3,0.55
smg,p90,1.380,26,0.860,0.070,1,$300,230,50,$2350,3700,1,1,3,0.55
smg,ump45,1.300,35,0.850,0.090,1,$600,230,25,$1200,3700,1,1,3,0.55
rifle,ak47,1.550,36,0.980,0.100,2,$300,215,30,$2700,8192,1,1,3,0.45
rifle,aug,1.800,28,0.980,0.090,2,$300,220,30,$3300,8192,1,1,3,0.45
rifle,famas,1.400,30,0.960,0.090,2,$300,220,25,$2250,8192,1,1,3,0.45
rifle,galilar,1.550,30,0.980,0.090,2,$300,215,35,$2000,8192,1,1,3,0.45
rifle,m4a1,1.400,33,0.970,0.090,2,$300,225,30,$3100,8192,1,1,3,0.45
rifle,m4a1_silencer,1.400,33,0.990,0.090,2,$300,225,20,$2900,8192,1,1,3,0.45
rifle,sg556,2.000,30,0.980,0.090,2,$300,210,30,$3000,8192,1,1,3,0.45
lmg,m249,1.600,32,0.970,0.080,2,$300,195,100,$5200,8192,1,1,1,0.40
lmg,negev,1.500,35,0.970,0.060,2,$300,195,150,$5700,8192,1,1,1,0.40
sniper,awp,1.950,115,0.990,1.455,2.5,$100,200,10,$450,8192,0,1,0,0.45
sniper,g3sg1,1.650,80,0.980,0.250,2.5,$300,215,20,$5000,8192,1,1,0,0.45
sniper,scar20,1.650,80,0.980,0.250,2.5,$300,215,20,$5000,8192,1,1,0,0.45
sniper,ssg08,1.700,88,0.980,1.250,2.5,$300,230,10,$1700,8192,0,1,0,0.45"""

class Weapon:
    def __init__(self, type, name, weaponarmorratio, damage, rangemodifier,
                cycletime, penetration, killaward, maxplayerspeed, clip_size,
                weaponprice, range, fullauto, bullets, tracerfrequency,
                flinchvelocitymodifierlarge):
        self.type = type
        self.name = name
        self.weaponarmorratio = float(weaponarmorratio)
        self.basedamage = float(damage)
        self.rangemodifier = float(rangemodifier)
        self.cycletime = float(cycletime)
        self.penetration = float(penetration)
        self.killaward = killaward
        self.maxplayerspeed = float(maxplayerspeed)
        self.clip_size = float(clip_size)
        self.weaponprice = weaponprice
        self.range = float(range)
        self.fullauto = float(fullauto)
        self.bullets = float(bullets)
        self.tracerfrequency = float(tracerfrequency)
        self.flinchvelocitymodifierlarge = float(flinchvelocitymodifierlarge)

    def _hitboxmodifier(self, location):
        if(location == 'head'):
            hitboxmod = 4.00
        if(location == 'chest'):
            hitboxmod = 1.00
        if(location == 'stomach'):
            hitboxmod = 1.25
        if(location == 'leg'):
            hitboxmod = 0.75
        return hitboxmod

    def damagerange_calc_witharmor(self, rangefire, location):
        damage = self.basedamage * self.weaponarmorratio/2 * self._hitboxmodifier(location) * self.rangemodifier**(rangefire/float(500))
        return damage

    def damagerange_calc_noarmor(self, rangefire, location):
        damage = self.basedamage * self._hitboxmodifier(location) * self.rangemodifier**(rangefire/float(500))
        return damage

wstats = [stat for stat in csv.reader(STATS.split('\n'), delimiter=',')]
weapons = [Weapon(*row) for row in wstats[1:]]
