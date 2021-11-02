from helpers.PopulaEnvironment import PopulaEnvironment
from algoritmo.AlgoritmoGuloso import AGuloso

def main():
    environment = PopulaEnvironment().make()
    search = AGuloso(environment)
    search.search('U', 'A')

main()