from dataclasses import dataclass, field
import uuid
from uuid import UUID

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid.uuid4) #para gerar um id automatico, ver na documentação do dataclass

    def __post_init__(self):
        self.validate()
    # def __init__(
    #         self, 
    #         name,
    #         id = "",
    #         description = "",
    #         is_active = True,
                 
    # ):
    #     self.id = id or uuid.uuid4()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active
    #     self.ledger = []

    #     self.validate()

    def validate(self): #serve para valida que o nome deve ter menos de 256 caracteres
        if len(self.name) >255:
            raise ValueError("name must have less than 256 characters")
        
        if len(self.name) == 0:
            raise ValueError("name cannot be empty")
        
        

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"
    
    # com esse mostra a representação da instacia, ou seja, não precis por print para mostrar o objeto
    def __repr__(self):
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __eq__(self, other): #a ==b a.__eq__(b)
        if not isinstance(other, Category): #Se o meu outro não for uma instacia de Category
            return False
        return self.id == other.id
    
    def update_category(self, name, description):
        self.name = name
        self.description = description


        self.validate()
    
    def activate(self):
        self.is_active = True

        self.validate()
    
