from solver import Solver

print(' Problema BeeCrowd  Programação Dinamica ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de PAA')
print('Autores: Daniel Antônio de Sá')
# Entrada
linha = input("Digite a entrada da primeira linha ").strip()
linha2 = input("Digite a entrada da segunda linha ").strip()
solver = Solver()
# Saída
print(solver.menor_string_subsequente(linha, linha2))
