class Knn():
    ## cliente eh um objeto da classe Cliente
    def __init__(self, data, no_class, k):
        self.data = data
        self.no_class = no_class
        self.k = k
        
    
    
    def aplicar_knn(self):
        '''
        Método principal para a chamada de todos os outros métodos.
            - distancia (Método para calcular a distancia entre os pontos e retornar uma lista, com todos esses resultados)
            - valores_proximos(Método para ordenar e devolver apenas os K(valor definido na entrada) menores elementos)
            - definir_tipo_investimento(Método para definir o tipo de investimento adequado do usuário)
            - dicionario_usuario_investimento(Método para retornar um dicionario com os CPF e o tipo de investimento ideal para os novos usuários)
        '''
        data_com_index = list(enumerate(self.data))
        novos_usuarios = {}

        for cpf1, tipo_investimento1, investimentos_nao_definido in self.no_class:
            listas = []
            for index, (cpf, tipo_investimento,investimentos)  in data_com_index:
            # Chamada do método Diistancia( Calcular a distancia entre os pontos)
                listas.append(self.distancia(index, investimentos, investimentos_nao_definido))
     
        #Método para ordenar e devolver apenas os 5 menores elementos    
            valores = self.valores_proximos(listas, self.k)
    
        #Método para definir o tipo de investimento do usuario
            investimento_ideal = self.definir_tipo_investimento(valores, data_com_index)
    
        #Método para retornar um dicionario com os CPF e os tipos de investimento dos novos usuarios
            self.dicionario_usuario_investimento(cpf1, investimento_ideal, novos_usuarios)
            
        return novos_usuarios
        
                                        
    def distancia(self, index, invest_definido, invest_nao_definido):
        '''
        Método para calcular a distancia entre os pontos e retornar uma lista, com todos esses resultados.
        
        Variaveis de Entrada:
            - index( Index da tabela de data)
            - invest_definido (Tupla dos valores de investimento da tabela data)
            - invest_nao_definido(Tupla dos valores de investimento da tabela no_class)
            
        Variaveis de saida:
            - lista_distancias(Lista com todas as distancias do invest_definido em relação aos valores do invest_nao_definido)
        '''
        resultado_distancia = 0
        lista_distancias = []
    
        for elemento in range(len(invest_definido)):
            resultado_distancia += (invest_definido[elemento] - invest_nao_definido[elemento])**2
            
        lista_distancias.append(index)    
        lista_distancias.append(resultado_distancia ** 0.5)
    
        return lista_distancias
    
    def valores_proximos(self, valores, k):
        '''
        Método para ordenar e devolver apenas os K(valor definido na entrada) menores elementos.
        
            Variaveis de Entrada:
                - valores(Lista com todas as distancias do invest_definido em relação aos valores do invest_nao_definido)
                - k(Valor recebido na entrada para definir quantas distancias devem ser comparadas)
            
            Variaveis de saida:
                - Retorna uma lista com as K menores distancias do invest_definido em relação aos valores do invest_nao_definido.
        '''
        return sorted(valores, key=lambda x:x[1])[:k]
    
    #Função para definir o tipo de investimento do usuário
    def definir_tipo_investimento(self, valores, data_com_index):
        '''
        Método para definir o tipo de investimento adequado do usuário.
        
            Variaveis de Entrada:
                - valores(Lista com as K menores distancias do invest_definido em relação aos valores do invest_nao_definido)
                - data_com_index(Lista data com um index)
            
            Variaveis de saida:
                - Retorna o tipo de investimento do investidor.
        '''
        lista_tipo_investimento = []
    
        for index, distancia in valores:
            lista_tipo_investimento.append(data_com_index[index][1][1])

        return max(set(lista_tipo_investimento), key = lista_tipo_investimento.count)            
    
    #Função para retornar um dicionario com os CPF e o tipo de investimento ideal para os novos usuários
    def dicionario_usuario_investimento(self, cpf1, investimento_ideal, novos_usuarios):
        '''
        Método para retornar um dicionario com os CPF e o tipo de investimento ideal para os novos usuários.
        
            Variaveis de Entrada:
                - cpf1(CPF do no_class)
                - investimento_ideal(Tipo de investimento do usuário)
                - novos_usuarios(Dicionario que ira ser preenchido com todos os usuários novos e seu tipo de investimento ideal)
            
            Variaveis de saida:
                - novos_usuarios(Dicionario que ira ser preenchido com todos os usuários novos e seu tipo de investimento ideal)
        '''
        novos_usuarios[cpf1] = investimento_ideal
    
        return novos_usuarios