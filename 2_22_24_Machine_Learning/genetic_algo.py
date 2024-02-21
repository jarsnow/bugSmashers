import random
valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, .-;:_!#%&/()=?@${[]}"
valid_chars_arr = list(valid_chars)
target_str = "hello world"

class Individual:

    def __init__(self):
        self.gene = self.generate_gene(len(target_str))
        self.fitness = self.determine_fitness()

    def generate_gene(self, length : int):
        genome = ""
        for i in range(length):
            genome += random.choice(valid_chars_arr)
        return genome
    def determine_fitness(self):
        fitness = 0
        for index, char in enumerate(self.gene):
            if target_str[index] != char:
                fitness += 1
        return fitness
    def __repr__(self):
        return f"{self.gene}:\t{self.fitness}"
    
def generate_population(size : int):
    population = []
    for i in range(size):
        my_individual = Individual()
        population.append(my_individual)
    return population
 
def best_of_population(population : list):
    population.sort(key = lambda x: x.fitness)
    population = population[:len(population)//5]
    return population

def mate(population):
    individual1 = random.choice(population)
    individual2 = random.choice(population)
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
    my_ind.fitness = my_ind.determine_fitness()
    return my_ind

def generate_new_population(old_population, size):
    my_pop = best_of_population(old_population)
    new_pop = []
    for i in range(size):
        
        my_ind = mate(my_pop)
        

        new_pop.append(my_ind)
    return new_pop

def check_fitness(population):
    for i in range(10):
        ind = random.choice(population)
        print(ind.gene)
        if ind.fitness == 0:
            return True, ind.gene
    print("\n")
    return False, ind.gene
    
def main():
    my_pop = generate_population(100)
    
    for i in range(150):
        print(f"Iteration {i}")
        my_pop = generate_new_population(my_pop, 100)
        finished, gene = check_fitness(my_pop)
        if finished == True:
            print(f"Found target string!, {gene}")
            break
        
main()