import random
valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, .-;:_!#%&/()=?@${[]}"
valid_chars_arr = list(valid_chars)
target_str = "hello world"

class Individual:

    def __init__(self):
        self.gene =""
        self.fitness = len(target_str)
    def generate_gene(self):
        genome = ""
        for i in range(len(target_str)):
            genome += random.choice(valid_chars_arr)
            
        self.gene = genome
    def determine_fitness(self):
        fitness = 0
        for index, char in enumerate(self.gene):
            if target_str[index] != char:
                fitness += 1
        self.fitness = fitness
    def __repr__(self):
        return f"{self.gene}:\t{self.fitness}"
    
def generate_population(size : int):
    population = []
    for i in range(size):
        my_individual = Individual()
        my_individual.generate_gene()
        my_individual.determine_fitness()
        population.append(my_individual)
    return population
 
def best_of_population(population : list):
    population.sort(key = lambda x: x.fitness)
    population = population[:len(population)//2]
    print(population)
    return population

def mate(individual1, individual2):
    out_gene = ""
    for index, char in enumerate(target_str):
        my_num = random.randint(0, 100)
        if my_num < 45:
            out_gene += individual1.gene[index]
        elif my_num >= 45 and my_num < 90:
            out_gene += individual2.gene[index]
        else:
            out_gene += random.choice(valid_chars_arr)
    my_ind = Individual()
    my_ind.gene = out_gene
    my_ind.determine_fitness()
    return my_ind

def generate_new_population(old_population, size):
    old_population = best_of_population(old_population)
    new_pop = []
    for i in range(size):
        
        individual1 = random.choice(old_population)
        individual2 = random.choice(old_population)
        
        new_individual = mate(individual1, individual2)
        new_pop.append(new_individual)
        
    return new_pop

def check_fitness(population):
    for i in range(10):
        ind = random.choice(population)
        if ind.fitness == 0:
            return True, ind.gene
    return False, ind.gene
    
def main():
    my_pop = generate_population(100)
    
    for i in range(150):
        my_pop = generate_new_population(my_pop, 100)
        finished, gene = check_fitness(my_pop)
        if finished == True:
            print("Found target string!")
            break
        
main()
        
    