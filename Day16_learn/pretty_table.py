from prettytable import PrettyTable

x=PrettyTable()
x.add_column("Pokemon Name",["Pikachu","Squirle"])
x.add_column("Type",["Electric","Water"])
x.align = "l"
print(x)