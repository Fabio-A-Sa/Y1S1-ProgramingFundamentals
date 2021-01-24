# Created on January, 2021
# @author: Fábio Araújo de Sá

# Import module random
import random

def cows_bulls(seed):
    
    # Random seed from FPRO
    random.seed(seed)
    
    def how_many(guess):

        certo = random.randint(0000, 9999)
        
        correct = [x for x in str(certo)]
        number = [x for x in str(guess)]
        
        # Cows - Correct number in correct position
        cows = 0
        for index, value in enumerate(number):

            if value == correct[index]:                
                if index == correct.index(value):
                        
                        cows = cows + 1
                        correct[index] = "x"
                        
        # Bulls - Correct number in wrong position
        bulls = 0        
        for index, value in enumerate(number):
           
            if value in correct:      
                bulls = bulls + 1
                correct[correct.index(value)] = "x"
                    
        return cows, bulls
    
    return how_many
