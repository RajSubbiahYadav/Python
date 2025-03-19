from typing import List , Tuple, Union, Dict

#List of integers
number: list[int] = [1, 2, 3, 4, 5]

#tuple pf string keys and integer values
person: tuple[str,int] = ("Raj", 22)

#Dictionary with string keys and integer values
score: dict[str,int] = {"Raj":99, "Kaushik":98}

#union type for variables that can hold multiple types
identifier: Union[int,str]= "ID1235"
identifier = 1235 #Also Valid

n : int = 5 

name : str = "Raj"

def sum(a:int , b:int) ->int:
    return a + b