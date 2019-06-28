from django.db import models


'''
 Classes for everything in the backend, this are gonna be A LOT of models.
'''


class Country(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=45)


class ArmedForce(models.Model):
    name = models.CharField(max_length=45)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING)
    date_established = models.DateField()


class Manufacturer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 45)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)


'''
 Base class for manufactured stuff
'''


class ManufacturedThing(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=45)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    # variant_of = models.OneToOneField(self.Thing ,on_delete=models.DO_NOTHING)
    variant = models.CharField(max_length=45)
    weight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    start_production = models.DateField()
    end_production = models.DateField()
    in_service = models.DateField()
    out_service = models.DateField()
    in_use_by = models.ManyToManyField(ArmedForce)


'''
 Subclasses of manufactured stuff
'''


class Projectile(ManufacturedThing):
    caliber = models.CharField(max_length=45)
    type = models.CharField(max_length=45)  # Make own class


class Weapon(ManufacturedThing):
    round = models.ForeignKey(Projectile, on_delete=models.DO_NOTHING)
    barrel_length = models.FloatField()


class Engine(ManufacturedThing):
    displacement = models.IntegerField()


class Type(models.Model):
    type_string = models.CharField(max_length=45)


class WarMachine(ManufacturedThing):
    armament = models.ManyToManyField(Weapon, on_delete=models.DO_NOTHING)
    crew = models.IntegerField()
    type = models.ManyToManyField(Type, on_delete=models.DO_NOTHING)


class Motorized(ManufacturedThing):
    engine = models.ManyToManyField(Engine)
    empty_weight = models.FloatField()
    loaded_weight = models.FloatField()


class Aircraft(Motorized, WarMachine):
    service_ceiling = models.FloatField()
    wing_area = models.FloatField()


class Ships(Motorized, WarMachine):
    commissioned = models.DateField()
    decommissioned = models.DateField()  # need to find way for multiple instances of com/decom
    draft = models.FloatField()


class Vehicles(Motorized, WarMachine):
    wheelbase = models.FloatField()
    track = models.FloatField()
