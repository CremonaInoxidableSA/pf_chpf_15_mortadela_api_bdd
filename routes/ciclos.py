from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from config.db import SessionLocal

from models.ciclos import Ciclos
from models.nivelesciclos import NivelesCiclos
from models.diccionarioestados import DiccionarioEstados
from models.recetas import Recetas
from models.torres import Racks
from models.diccionariocancelaciones import DiccionarioCancelaciones

router = APIRouter(prefix="/ciclos_por_fecha", tags=["ciclos"])


def get_db():
    """Obtener sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_ciclos_por_fecha(fecha: str):
    """
    Obtiene todos los ciclos contemplados en el día indicado por fecha de inicio.
    - **fecha**: La fecha va en formato YYYY-MM-DD. RESPETAR.
    """
    db = SessionLocal()
    try:
        # Validar y parsear la fecha
        try:
            fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Formato de fecha inválido. Use YYYY-MM-DD"
            )
        
        # Definir rango de fechas para todo el día
        fecha_inicio_dia = datetime.combine(fecha_dt, datetime.min.time())
        fecha_fin_dia = fecha_inicio_dia + timedelta(days=1)
        
        # Consultar ciclos
        ciclos = db.query(Ciclos).filter(
            Ciclos.fecha_inicio >= fecha_inicio_dia,
            Ciclos.fecha_inicio < fecha_fin_dia
        ).order_by(Ciclos.fecha_inicio).all()
        
        # Serializar resultados
        ciclos_data = [
            {
                "id_ciclo": ciclo.id_ciclo,
                "fecha_inicio": ciclo.fecha_inicio.isoformat() if ciclo.fecha_inicio else None,
                "fecha_fin": ciclo.fecha_fin.isoformat() if ciclo.fecha_fin else None
            }
            for ciclo in ciclos
        ]
        
        return {
            "ciclos": ciclos_data,
            "numero_ciclos": len(ciclos_data)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )
    finally:
        db.close()

@router.get("/datos")
def get_datos_ciclo(id_ciclo: int):
    """
    Obtiene los detalles completos de un ciclo específico.
    
    **id_ciclo**: El ID del ciclo a consultar.
    """
    db = SessionLocal()
    try:
        ciclo = db.query(Ciclos).filter(Ciclos.id_ciclo == id_ciclo).first()
        if not ciclo:
            raise HTTPException(
                status_code=404,
                detail="Ciclo no encontrado"
            )
        
        estado_obj = db.query(DiccionarioEstados).filter(
            DiccionarioEstados.id_estado == ciclo.id_estado
        ).first()
        estado = estado_obj.descripcion if estado_obj else None
        
        receta = db.query(Recetas).filter(
            Recetas.id_receta == ciclo.id_receta
        ).first()
        tipo_corte = receta.codigo_producto if receta else None
        
        rack = db.query(Racks).filter(
            Racks.id_rack == ciclo.id_rack
        ).first()
        nombre_rack = rack.nombre_rack if rack else None
        
        # Obtener todos los niveles del ciclo
        niveles = db.query(NivelesCiclos).filter(
            NivelesCiclos.id_ciclo == id_ciclo
        ).order_by(NivelesCiclos.nivel).all()
        
        # Contar niveles seleccionados
        niveles_posibles = sum(1 for nivel in niveles if nivel.seleccionado)
        
        # Construir array de niveles con sus detalles
        niveles_data = []
        for nivel_obj in niveles:
            # Obtener descripciones de cancelaciones
            cancelaciones_descripciones = []
            if nivel_obj.cancelaciones:
                # cancelaciones es un JSON/array con IDs
                for id_cancel in nivel_obj.cancelaciones:
                    cancel_obj = db.query(DiccionarioCancelaciones).filter(
                        DiccionarioCancelaciones.id_cancelaciones == id_cancel
                    ).first()
                    if cancel_obj:
                        cancelaciones_descripciones.append(cancel_obj.descripcion)
            
            niveles_data.append({
                f"nivel{nivel_obj.nivel}": {
                    "resultado": nivel_obj.finalizado,
                    "tiempo_nivel": nivel_obj.tiempo_nivel,
                    "cancelaciones": cancelaciones_descripciones
                }
            })
        
        return {
            "estado": estado,
            "tipo_corte": tipo_corte,
            "peso_procesado": ciclo.peso_procesado if hasattr(ciclo, 'peso_procesado') else None,
            "tiempo_total": ciclo.tiempo_total,
            "tiempo_pausa": ciclo.tiempo_pausa,
            "rack": nombre_rack,
            "niveles_posibles": niveles_posibles,
            "niveles": niveles_data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )
    finally:
        db.close()