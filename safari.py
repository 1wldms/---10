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
    
    def 만들기!

    """
    def __init__(self, grid_size=5):
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid_size = grid_size
        self.timestep = 0

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
        
        for zebra in self.zebra:
            zebra.move(self.grid)
        
        for lion in self.lion:
            lion.move(self.grid)
        
        for zebra in self.zebra:
            self.grid[zebra.y][zebra.x] = 'Z'
        
        for lion in self.lion:
            self.grid[lion.y][lion.x] = 'Z'



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
        # 이부분 채우기
        pass
        
    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target='.')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self,y = chosen_neighbor
            return True
        return False
        
    def get_neighbors(self, grid, target):
        ''' target can be ., L, or Z
        returns a list of coordinates '''
        print_TODO('get_neighbors currently returns all directinos')
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x - 1, y])
        neighbors.append([x + 1, y])
        neighbors.append([x, y - 1])
        neighbors.append([x, y + 1])
        return neighbors


class Lion(animal):
    def __init__(self, x, y):
        super().__int__(x,y)
        self.hp = 3
        
    def move(self, grid):
        print_TODO('get neighboring zebra')
        print_TODO('move to zebra if found')
        if self.move_to(grid, target='Z'):
            self.hp = 3
            return

        print_TODO('get empty neighbor')
        self.move_to(grid, target='.')


class Zebra(animal):
    def __init__(self, x, y):
        super().__int__(x,y)
        
    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        self.move_to(grid, target='.')
        print(f'after: {self.x=}, {self.y=}')

s = Safari()
s.display()




