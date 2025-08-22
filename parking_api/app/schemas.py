from pydantic import BaseModel
from datetime import datetime
#valida os dados que entram e saem da API
class VehicleCreate(BaseModel):
    plate: str              #Quando o veiculo E criado ele so precisa da placa

class VehicleUpdate(BaseModel):
    exit_time: datetime | None = None
    payment_amount: float | None = None
    is_paid: bool | None = None

class Vehicle(BaseModel):
    id: int
    plate: str
    entry_time: datetime
    exit_time: datetime | None   #Quando devolver para o usuario mostra todos os campos
    payment_amount: float | None
    is_paid: bool

    class Config:
        from_attributes = True  # Para compatibilidade com SQLAlchemy
