import random

class AtmosphericSensor:
    def __init__(self):
        self.CO2_level = random.uniform(0, 100)
        self.N2_level = random.uniform(0, 100)
        self.Ar_level = random.uniform(0, 100)
        self.O2_level = random.uniform(0, 100)
        self.H2O_level = random.uniform(0, 100)

    def check_gas_levels(self):
        gas_levels = {'CO2': self.CO2_level, 'N2': self.N2_level, 'Ar': self.Ar_level, 'O2': self.O2_level, 'H2O': self.H2O_level}
        for gas, level in gas_levels.items():
            if gas == 'CO2' and level > 95:
                print(f"Предупреждение: Уровень {gas} в атмосфере превысил норму.")
            elif gas == 'N2' and level > 2.7:
                print(f"Предупреждение: Уровень {gas} в атмосфере превысил норму.")
            elif gas == 'Ar' and level > 1.6:
                print(f"Предупреждение: Уровень {gas} в атмосфере превысил норму.")
            elif gas == 'O2' and level > 0.2:
                print(f"Предупреждение: Уровень {gas} в атмосфере превысил норму.")
            elif gas == 'H2O' and level > 0.1:
                print(f"Предупреждение: Уровень {gas} в атмосфере превысил норму.")

class SolarPanels:
    def __init__(self):
        self.energy_output = random.uniform(0, 100)
        self.dust_layer = random.uniform(0, 10)

    def generate_energy(self):
        print(self.dust_layer)
        if self.dust_layer > 5:  # Проверка слоя пыли
            raise Exception("Слой пыли слишком большой, чтобы запустить солнечную панель.")
        return self.energy_output

class WaterPurificationSystem:
    def __init__(self):
        self.water_temperature = random.randint(3, 50)  # температура в градусах Цельсия
        self.ph_level = random.randint(1, 12)  # уровень pH
        self.bacteria_count = random.randint(0, 10000)  # количество бактерий в 1 мл воды
        self.water_quality = self.check_water_quality()

    def check_water_quality(self):
        if 6 <= self.ph_level <= 8 and self.bacteria_count < 5000 and 18 <= self.water_temperature <= 22:
            return "Отличное"
        elif 5 <= self.ph_level <= 9 and self.bacteria_count < 10000 and 15 <= self.water_temperature <= 25:
            return "Среднее"
        else:
            return "Плохое"

class Greenhouse:
    def __init__(self):
        self.food_production = random.uniform(0, 100)
        self.oxygen_production = random.uniform(0, 100)
        self.light_intensity = random.uniform(0, 10000)  # интенсивность освещения в люксах

    def check_light_intensity(self):
        if self.light_intensity < 1000:
            raise ValueError("Недостаточная интенсивность света. Лампы не работают или света недостаточно.")

class OrbitalMind:
    def __init__(self):
        self.atmospheric_sensor = AtmosphericSensor()
        self.solar_panels = SolarPanels()
        self.water_purification_system = WaterPurificationSystem()
        self.greenhouse = Greenhouse()

class LifeSupportSystem:
    @staticmethod
    def check_atmospheric_sensor(co2_level, n2_level, ar_level, o2_level, h2o_level):
        warnings = []
        gas_levels = {'CO2': co2_level, 'N2': n2_level, 'Ar': ar_level, 'O2': o2_level, 'H2O': h2o_level}
        for gas, level in gas_levels.items():
            if gas == 'CO2' and level > 95:
                warnings.append('CO2')
            elif gas == 'N2' and level > 2.7:
                warnings.append('N2')
            elif gas == 'Ar' and level > 1.6:
                warnings.append('Ar')
            elif gas == 'O2' and level > 0.2:
                warnings.append('O2')
            elif gas == 'H2O' and level > 0.1:
                warnings.append('H2O')
        return warnings if warnings else "Нормальные значения"

    @staticmethod
    def check_solar_panels(dust_layer):
        if dust_layer > 5:
            return "Слой пыли слишком большой, чтобы запустить солнечную панель."
        return "Нормальное значение"

    @staticmethod
    def check_water_purification_system(water_purification_system):
        if water_purification_system.ph_level < 6 or water_purification_system.ph_level > 8:
            return "Плохое"
        elif water_purification_system.bacteria_count > 5000:
            return "Плохое"
        elif water_purification_system.water_temperature < 15 or water_purification_system.water_temperature > 25:
            return "Плохое"
        else:
            return "Отличное"

    @staticmethod
    def check_greenhouse(light_intensity):
        if light_intensity < 1000:
            return "Недостаточная интенсивность света. Лампы не работают или света недостаточно."
        return "Нормальное значение"



if __name__ == '__main__':
    orbital_mind = OrbitalMind()
