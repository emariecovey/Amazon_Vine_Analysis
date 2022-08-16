from mrjob.job import MRJob

#class/instance notes:
##classes are used to define properties and behavior of a category of things

#E.g. A "Car" class might dictate that all cars be defined by their make, model, year, and mileage.
#But you can't provide specifics about a particular car (for example, that 1978 Chevy Impala with 205,000 miles on it that your uncle Mickey drives) 
##until you create an "instance" of a Car. It's the instance that captures the detailed information about one particular Car.

#you know what people are. You are an "instance" of the class "people" - I can talk about people in general (the class of objects), 
#or if I have a specific one in mind, I talk of an "instance". An instance can have properties that are not automatically 
#a consequence of being a member of the class. All humans have a heart, but not all humans have your name and date of birth.


#This class inherits (takes properties from) the mrjob class. It can be called to run the mapreduce job
class Bacon_count(MRJob):
    #function to assign input into key-value pairs
    def mapper(self, _, line): #line is line of text to be examined
        for word in line.split(): #splits all text into individual words
            if word.lower()=="bacon": #converts all words to lowercase and then tests to see if they're bacon
                yield "bacon", 1 #mrjob works in key-value pairs. https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement
        #There's a shuffle step that occurs after the mapper. There is no code written for this step, and it occurs because the class inherits from the mrjob library. This shuffle step organizes the key-value pairs so that there's only one key for each unique key, and combines the values into a list.
    def reducer(self, key, values): #self represents the instance of class
        yield key, sum(values)
    #conventional Python code for running the program:
if __name__=="__main__":
    Bacon_count.run()

#to run this file, type in terminal: python bacon_counter.py input.txt
#for some reason, there's a problem running it in the terminal inside of vs code (even when changing the 
#interpreter to be in the right environment, so run it in a regular terminal window)