import random
valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, .-;:_!#%&/()=?@${[]}"
valid_chars_arr = list(valid_chars)
target_str = "hello world"

class Individual:
    def __init__(self):
        self.gene = ""
        self.fitness = len(target_str)
        
    def generate_gene(self):
        new_gene = ""
        for char in target_str:
            new_gene += random.choice(valid_chars_arr)
        self.gene = new_gene
    def determine_fitness(self):
        new_fitness = 0
        for index, char in enumerate(target_str):
            if self.gene[index] != char:
                new_fitness += 1
        self.fitness = new_fitness
        
    def __repr__(self):
        return f"{self.gene}, {self.fitness}"
    
def generate_first_pop(size):
    new_pop = []
    for i in range(size):
        my_individual = Individual()
        my_individual.generate_gene()
        my_individual.determine_fitness()
        new_pop.append(my_individual)
    return new_pop

def mate(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    my_individual = Individual()
    for i in range(len(target_str)):
        my_num = random.randint(0, 100)
        
        if my_num < 45:
            my_individual.gene += parent1.gene[i]
        elif my_num >= 45 and my_num < 90:
            my_individual.gene += parent2.gene[i]
        else:
            my_individual.gene += random.choice(valid_chars_arr)
    my_individual.determine_fitness()
    return my_individual

def evolve(population):
    population.sort(key=lambda x: x.fitness)
    natural_selection = population[:len(population)//4]
    new_pop = []
    for i in range(len(population)):
        new_pop.append(mate(natural_selection))
        
    return new_pop

my_pop = generate_first_pop(1000)

for i in range(150):
    my_pop = evolve(my_pop)
    
    for i in range(100):
        to_check = random.choice(my_pop)
        print(to_check)
        if to_check.fitness == 0:
            print(f"FOUND TARGET\n\t{to_check}")
            quit()