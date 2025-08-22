from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from datetime import datetime

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_plate(db, vehicle.plate)
    if db_vehicle:
        raise HTTPException(status_code=400, detail="Veículo já registrado")
    return crud.create_vehicle(db, vehicle) #Ele cria um veiculo se a pessoa entrar nessa URL, 

@router.get("/{plate}", response_model=schemas.Vehicle)
def read_vehicle(plate: str, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_plate(db, plate)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return db_vehicle # consulta o carro pela placa

@router.get("/", response_model=list[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Vehicle).offset(skip).limit(limit).all() #tem a função de listar todos oas carros no estacionamento

@router.put("/{plate}/checkout", response_model=schemas.Vehicle)
def checkout_vehicle(plate: str, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_plate(db, plate)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    if db_vehicle.is_paid:
        raise HTTPException(status_code=400, detail="Já pago")
    db_vehicle.exit_time = datetime.utcnow()
    time_spent = (db_vehicle.exit_time - db_vehicle.entry_time).total_seconds() / 3600
    db_vehicle.payment_amount = time_spent * 5  # Taxa de R$5/hora
    db_vehicle.is_paid = True
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle #tem a função de fazer o checkout e calcular o falor por hora, que no caso é R$5/hora

@router.patch("/{plate}/release", response_model=schemas.Vehicle)
def release_vehicle(plate: str, vehicle_update: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_plate(db, plate)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    if not db_vehicle.is_paid:
        raise HTTPException(status_code=400, detail="Pagamento pendente")
    # Atualiza campos opcionais
    if vehicle_update.exit_time:
        db_vehicle.exit_time = vehicle_update.exit_time
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle#tem a função de kiberar a cancela caso tenha sido pago

@router.delete("/{plate}")
def delete_vehicle(plate: str, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_plate(db, plate)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    db.delete(db_vehicle)
    db.commit()
    return {"detail": "Veículo removido"} #tem a função de remover o registro do carro no banco
