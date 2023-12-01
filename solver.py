class Solver:

    def menor_string_subsequente(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)] # cria a matriz n+1 X m+1 para amarzenar os valores

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]: # verifica se o valor de cada item da primeira string é igual a cada valor da segunda string
                    dp[i][j] = 1 + dp[i - 1][j - 1] # somo 1 ao valor anterior, valor inicia na posição (1,1) para consseguir verificar a anterior sem acessar uma posição invalida
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # caso não seja igual ele verifica o valor maximo da linha anterior da posição atual
                                                                # com o ultimo valor inserido

        return m + n - dp[m][n] # retona a soma das duas strigs menos a quantidade de repetições

