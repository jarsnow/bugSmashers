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
        for index, obj in enumerate(target_str):
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
    pop = []
    for i in range(size):
        my_ind = Individual()
        my_ind.generate_gene()
        my_ind.determine_fitness()
        pop.append(my_ind)
    return pop

def mate(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)

    my_ind = Individual()

    for i, o in enumerate(target_str):
        my_num = random.randint(0, 100)

        if my_num < 45 : 
            my_ind.gene += parent1.gene[i]
        elif my_num >= 45 and my_num < 90:
            my_ind.gene += parent2.gene[i]
        else:
            my_ind.gene += random.choice(valid_chars_arr)

    my_ind.determine_fitness()
    return my_ind

def evolve(population):
    population.sort(key= lambda x: x.fitness)
    natural_selection = population[::len(population)//2]
    new_pop = []
    for i in range(len(population)):
        new_pop.append(mate(natural_selection))
    return new_pop

my_pop = generate_first_pop(100)

num_iterations = 150

for i in range(num_iterations):
    my_pop = evolve(my_pop)

    for i in range(10):
        to_check = random.choice(my_pop)
        print(to_check)
        if to_check.fitness == 0:
            print(f"FOUND TARGET\n\t{to_check}")
            quit()


    