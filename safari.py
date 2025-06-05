class safari:
    """ 
    !!!사파리 관리!!!
    이 클래스 안에
    
    하람
    grid
    맨 처음 무작위 배치
    __init__
    move_to
    
    지은
    timestep
    step_move
    step_breed
    
    def 만들기!
    """
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
    
    def run (self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()


class animal:
    def __init__(self, x, y):
        # 이부분 채우기
        
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
    def move(self, grid):
        print_TODO('get neighboring zebra')
        print_TODO('move to zebra if found')
        if self.move_to(grid, target='Z'):
            self.hp = 3
            return

        print_TODO('get empty neighbor')
        self.move_to(grid, target='.')


class Zebra(animal):
    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        self.move_to(grid, target='.')
        print(f'after: {self.x=}, {self.y=}')






