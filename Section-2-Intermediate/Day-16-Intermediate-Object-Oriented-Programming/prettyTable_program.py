from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Raichu"])
table.add_column("Type", ["Electric", "Water", "Electric"])

print(table)