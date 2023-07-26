class Assign:
    def __init__(self, days, letters):
        self.days = days
        self.letters = letters

    def possible_combinations(self):
        return self._generate_combinations(self.days)

    def _generate_combinations(self, days_left):
        if days_left == 0:
            return ['']
        
        result = []
        for letter in self.letters:
            for combination in self._generate_combinations(days_left - 1):
                result.append(letter + combination)

        return result

    def probability_to_miss_gradution_ceremony(self):
        last_day_absent_count = 0
        valid_combination = 0
        
        for combination in self.possible_combinations():
            if combination.find("AAAA")== -1:
                if combination[-1]=="A":
                    last_day_absent_count+=1
                valid_combination +=1

        print(f"The number of ways to attend classes over {self.days} days is {valid_combination}")
        print(f"The probability that you will miss your graduation ceremony is {last_day_absent_count}/{valid_combination}")
        

if __name__ == "__main__":
    try:
        days = int(input("Please enter the number of days: "))
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")
    except ValueError:
        print("'Days' must be a positive integer.")
    else:
        letters = ['A', 'P']
        ass = Assign(days, letters)
        ass.probability_to_miss_gradution_ceremony()

        