
class Device():
    def __init__(self, brand: str, model: str, power: int):
        self.brand = brand
        self.model = model
        self.power = power

    def __str__(self):
        return f'''
        Brand: {self.brand.title()}
        Model: {self.model.upper()}
        Power: {self.power} Wt
        '''

class CoffeMachine(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model, power)
        self.connection_type = '1-phase'
        self.water_volume = 2
        self.cup_cells = 1
        
    def __str__(self):
        return f'''
        Connection type: {self.connection_type} connection
        Water volume: {self.water_volume} liters
        Cells for cups: {self.cup_cells}
        '''
    def power_changer(self):
        if self.connection_type[0] == '3':
            self.power = int(self.power/220*380)
            return self.power
        return self.power   
    
    @property
    def connection(self):
        return self.connection_type
    @connection.setter
    def set_connection_type(self, value):
        typer = str(value) + '-phase'
        self.connection_type = typer
        self.power_changer()

    @property
    def water(self):
        return self.water_volume
    @water.setter
    def set_water_volume(self, value):
        self.water_volume = value

    @property
    def cups(self):
        return self.cup_cells
    @cups.setter
    def set_cup_cells(self, value):
        self.cup_cells = value
        

class Blender(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model, power)
        self.rotation_speed = 600
        self.container_volume = 1
        self.price = 1500
        
    def __str__(self):
        return f'''
        Rotation speed: {self.rotation_speed} rpm
        Container volume: {self.container_volume} liters
        Price: {self.price} ₴
        '''

    def power_changer(self):
        if self.rotation_speed != 600:
            self.power = self.power + int(self.rotation_speed/600*0.1*self.power)
            return self.power
        return self.power
    
    def price_changer(self):
        if self.container_volume != 1:
            self.price = self.price + int(self.container_volume/1*0.1*self.price)
            return self.price
        return self.price
        
    @property   
    def rotation(self):
        return self.rotation_speed      
    @rotation.setter
    def change_rotation_speed(self, value: int):
        self.rotation_speed = value
        self.power_changer()

    @property
    def volume(self):
        return self.container_volume
    @volume.setter
    def change_container_volume(self, value: int):
        self.container_volume = value
        self.price_changer()

    
class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model, power)
        self.blades_number = 1
        self.operating_modes = 1
        self.price = 1000
        
    def __str__(self):
        return f'''
        Number of blades: {self.blades_number}
        Operating modes: {self.operating_modes}
        Price: {self.price} ₴
        '''    
    
    def price_changer(self):
        if self.blades_number != 1:
            self.price = self.price + int(self.blades_number*0.1*self.price)
            return self.price
        if self.operating_modes != 1:
            self.price = self.price + int(self.operating_modes*0.1*self.price)
            return self.price
        return self.price    
    
    @property   
    def blades(self):
        return self.blades_number     
    @blades.setter
    def change_blades_number(self, value: int):
        self.blades_number = value
        self.price_changer()
        
    @property   
    def modes(self):
        return self.operating_modes     
    @blades.setter
    def change_operating_modes(self, value: int):
        self.operating_modes = value
        self.price_changer()
 

if __name__ == '__main__':
    cm = CoffeMachine('ariston', '345cj-we12', 2200)
    cm.set_connection_type = 3
    cm.set_water_volume = 5
    cm.set_cup_cells = 3
    #print(Device.__str__(cm))
    #print(cm)
    
    ble = Blender('bosch', 'efew-12313', 1200)
    ble.change_rotation_speed = 1000
    ble.change_container_volume = 3
    #print(Device.__str__(ble))
    #print(ble)
    
    gri = MeatGrinder('liberton', 'neo-320 nl', 1500)
    print(gri.blades_number)
    gri.change_blades_number = 3
    gri.change_operating_modes = 3
    print(Device.__str__(gri))
    print(gri)    
    
