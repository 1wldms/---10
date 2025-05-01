class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_num_passengers = 0
    
    def is_full(self):
        return self.current_num_passengers == self.capacity
    
    def load(self, count):
        print(f'{count} passengers are trying to get on.')
        if self.is_full():
            print(f'{self.name} is full. Take next one.')
            return
        if self.current_num_passengers + count <= self.capacity:
            self.current_num_passengers += count
            print(f'{self.name} loaded {count} passengers.')
        else:
            loading_count = self.capacity - self.current_num_passengers
            self.current_num_passengers = self.capacity
            print(f'{self.name} loaded {loading_count} passengers.')
            print(f'{count - loading_count} passengers should take next one.')
    
    def __str__(self):
        return f'{self.name}: {self.current_num_passengers} / {self.capacity}'

class Bus(Vehicle):
    def __init__(self, name, capacity, is_card_only=False):
        super().__init__(name, capacity)
        self.buzzer_status = False
        self.is_card_only = is_card_only
    
    def press_buzzer(self):
        print('zzzzzzzz! Stopping at the next stop.')
        self.buzzer_status = True
    
    def unload(self, count):
        self.buzzer_status = False
        assert self.current_num_passengers > count
        self.current_num_passengers -= count
        print(f'{self.name} unloaded {count} passengers.')
    
    def buzzer_is_on(self):
        return self.buzzer_status
    
    def __str__(self):
        return super().__str__() + f', buzzer_status={self.buzzer_status}'

class Taxi(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.destination = 'not set'
    
    def set_destination(self):
        self.destination = input('destination?')
        
    def get_destination(self):
        return self.destination
    
    def load(self, count):
        super().load(count)
        self.set_destination()
    
    def __str__(self):
        return super().__str__() + f', destination={self.destination}'
    
    def unload(self):
        print(f'{self.name} unloading {self.current_num_passengers} passengers.')
        self.current_num_passengers = 0
        self.destination = 'not set'
        

class PaymentError(Exception):
    def __str__(self):
        return 'Payment mismatch.'

class Passenger:
    def __init__(self, is_cash_only=False):
        self.is_cash_only = is_cash_only
    
    def get_on(self,bus: Bus):
        if self.is_cash_only and bus.is_card_only:
            raise PaymentError
        print(f'getting on {bus.name}')