from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.schemas.interaction_schema import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):

    new_interaction = Interaction(**interaction.model_dump())

    db.add(new_interaction)

    db.commit()

    db.refresh(new_interaction)

    return new_interaction


def get_all_interactions(db: Session):

    return db.query(Interaction).all()


def get_interaction(db: Session, interaction_id: int):

    return db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()


def update_interaction(
        db: Session,
        interaction_id: int,
        interaction: InteractionCreate
):

    obj = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not obj:
        return None

    for key, value in interaction.model_dump().items():
        setattr(obj, key, value)

    db.commit()

    db.refresh(obj)

    return obj


def delete_interaction(db: Session, interaction_id: int):

    obj = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not obj:
        return None

    db.delete(obj)

    db.commit()

    return obj