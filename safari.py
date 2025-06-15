import random

class Safari:
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

    
    def step_move(self):
    # 얼룩말 위치 지우기
        for zebra in self.zebras:
            self.grid[zebra.y][zebra.x] = '.'
        # 얼룩말 이동
        for zebra in self.zebras:
            zebra.move(self.grid)
        # 얼룩말 위치 표시
        for zebra in self.zebras:
            self.grid[zebra.y][zebra.x] = 'Z'

        # 사자 hp 체크 및 죽은 사자 위치 지우기
        surviving_lions = []
        for lion in self.lions:
            if lion.hp > 0:
                surviving_lions.append(lion)
            else:
                self.grid[lion.y][lion.x] = '.'
        self.lions = surviving_lions

        # 사자 위치 지우기 (이동 전)
        for lion in self.lions:
            self.grid[lion.y][lion.x] = '.'

        # 사자 이동
        for lion in self.lions:
            lion.move(self.grid, self.zebras)

        # 사자 위치 표시 (이동 후)
        for lion in self.lions:
            self.grid[lion.y][lion.x] = 'L'


    def step_breed(self):
        new_zebras = []
        for zebra in self.zebras:
            zebra.age += 1
            if zebra.age >= 3:
                neighbors = zebra.get_neighbors(self.grid, target='.')
                if neighbors:
                    x, y = random.choice(neighbors)
                    new_zebras.append(Zebra(x, y))
        
        new_lions = []
        for lion in self.lions:
            lion.age += 1
            if lion.age >= 5:
                neighbors = lion.get_neighbors(self.grid, target='.')
                if neighbors:
                    x, y = random.choice(neighbors)
                    new_lions.append(Lion(x, y))
        self.zebras += new_zebras
        self.lions += new_lions

    def timestep_adding(self):
        self.timestep += 1

    def run(self, num_timesteps=100):
        self.display()
        
        while self.timestep < num_timesteps:
            key = input("Press Enter to continue, or [q] to quit: ")
            if key.lower() == 'q':
                break
            self.timestep_adding()
            self.step_move()
            self.display()
            self.step_breed()



class animal:
    def __init__(self, x, y):
        self.age = 0
        self.x = x
        self.y = y

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target=target)  
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
        super().__init__(x, y)
        self.hp = 5

    def move(self, grid, zebras):
    # 1) 인접한 얼룩말 있으면 먹기
        zebra_neighbors = self.get_neighbors(grid, target='Z')
        if zebra_neighbors:
            chosen_pos = random.choice(zebra_neighbors)
            self.x, self.y = chosen_pos
            
            for zebra in zebras:
                if zebra.x == self.x and zebra.y == self.y:
                    zebras.remove(zebra)
                    grid[self.y][self.x] = '.'  # 그리드에서 얼룩말 자리 비우기
                    break

            self.hp = 3
            return

        # 2) 먹을 얼룩말이 인접에 없으면, 가장 가까운 얼룩말 쪽으로 한 칸 이동
        if zebras:
            # 가장 가까운 얼룩말 찾기 
            target = min(zebras, key=lambda z: abs(z.x - self.x) + abs(z.y - self.y))
            dx = target.x - self.x
            dy = target.y - self.y
            step_x = 1 if dx > 0 else -1 if dx < 0 else 0
            step_y = 1 if dy > 0 else -1 if dy < 0 else 0
            for nx, ny in [(self.x + step_x, self.y), (self.x, self.y + step_y)]:
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == '.':
                    self.x, self.y = nx, ny
                    break
        # 3) 이동 후 먹이 없었으니 hp 감소
        self.hp -= 1


class Zebra(animal):
    def __init__(self, x, y):
        super().__init__(x,y)
        
    def move(self, grid):
        self.move_to(grid, target='.')



if __name__ == "__main__":
    s = Safari()
    s.run()




