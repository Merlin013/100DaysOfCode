from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Raichu"], align="r")
table.add_column("Type", ["Electric", "Water", "Electric"])
#table.align = "l"
print(table)