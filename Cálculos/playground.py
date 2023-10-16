class Viga:
    """Cria uma viga que será analisada 
    """
    def __init__(self, comprimento):
        self.comprimento = comprimento
        
    
    def apoio(tipo:str, posição:float):
        """Apoio presente na viga

        Args:
            tipo (str): pino, rolete,engaste
            posição (float): posição do apoio na viga
        """
        