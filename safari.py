import random

class Safari:
    """ 
    !!!사파리 관리!!!
    이 클래스 안에
    
    하람
    grid
    맨 처음 무작위 배치
    __init__
    
    지은
    step_move
    step_breed

    """
    def __init__(self, grid_size=50):
        self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid_size = grid_size
        self.timestep = 0
        self.zebras = []
        self.lions = []

         # 무작위로 동물 배치
        for _ in range(20):  # 얼룩말 20마리
            x, y = self.get_random_empty_position()
            self.zebras.append(Zebra(x, y))
            self.grid[y][x] = 'Z'

        for _ in range(5):  # 사자 5마리
            x, y = self.get_random_empty_position()
            self.lions.append(Lion(x, y))
            self.grid[y][x] = 'L'

    def get_random_empty_position(self):
        while True:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if self.grid[y][x] == '.':
                return x, y
            

    def display(self):
        print(f'Clock: {self.timestep}')
        top_coord_str = ' '.join([f'{coord}' for coord in range(len(self.grid))])
        print('   ' + top_coord_str)
        for animal in self.zebras:
            self.grid[animal.y][animal.x] = 'Z'
        for animal in self.lions:
            self.grid[animal.y][animal.x] = 'L'
        for row, line in enumerate(self.grid):
            print(f'{row:2} ' + ' '.join(line))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()
    
    def step_move(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] in ('L','Z'):
                    self.grid[y][x] = '.'
        
        # 이동
        for zebra in self.zebras:
            zebra.move(self.grid)
        
        for lion in self.lions:
            lion.move(self.grid)
        
        # grid표시
        for zebra in self.zebras:
            self.grid[zebra.y][zebra.x] = 'Z'
        for lion in self.lions:
            self.grid[lion.y][lion.x] = 'L'
            
    def step_breed(self):
        new_zebras = []
        for zebra in self.zebras:
            zebra.age += 1
            if zebra.age >= 3:
                neighbors = self.get_neighbors(self.grid, target='.')
                if neighbors:
                    x, y = random.choice(neighbors)
                    new_zebras.append(Zebra(x, y))
        
        new_lions = []
        for lion in self.lions:
            lion.age += 1
            if lion.age >= 3:
                neighbors = self.get_neighbors(self.grid, target='.')
                if neighbors:
                    x, y = random.choice(neighbors)
                    new_lions.append(Lion(x, y))
        self.zebras += new_zebras
        self.lions += new_lions

    def timestep_adding(self):
        self.timestep += 1

    def run (self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep_adding()
            self.step_move()
            self.display()
            self.step_breed()
            self.display()


class animal:
    def __init__(self, x, y):
        self.age = 0
        self.x = x
        self.y = y

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target='.')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            return True
        return False

    def get_neighbors(self, grid, target):
        ''' target can be ., L, or Z
        returns a list of coordinates '''
        x, y = self.x, self.y
        neighbors = []
        candidate_positions = [
            [x - 1, y],
            [x + 1, y],
            [x, y - 1],
            [x, y + 1]
        ]
        
        for nx, ny in candidate_positions:
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] == target:
                    neighbors.append([nx, ny])
        return neighbors


class Lion(animal):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.hp = 3
        
    def move(self, grid):
        print('get neighboring zebra')
        zebra_neighbors = self.get_neighbors(grid, target='Z')
       
        print('move to zebra if found')
        if self.move_to(grid, target='Z'):
            self.hp = 3
            return

        print('get empty neighbor')
        self.move_to(grid, target='.')


class Zebra(animal):
    def __init__(self, x, y):
        super().__init__(x,y)
        
    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        self.move_to(grid, target='.')
        print(f'after: {self.x=}, {self.y=}')

s = Safari()
s.display()




