from sqlalchemy.orm import Session
from . import models, schemas
#Funcoes que criam, buscam, atualizam e deleta veiculos
def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(plate=vehicle.plate)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle #salva um carro

def get_vehicle_by_plate(db: Session, plate: str):
    return db.query(models.Vehicle).filter(models.Vehicle.plate == plate).first() #busca um carro

# Outras funções: update_vehicle, delete_vehicle, etc.
