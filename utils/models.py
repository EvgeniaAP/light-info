from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class BaseModel(DeclarativeBase):
    pass

# свойство
class Feature(BaseModel):
    __tablename__ = 'feature'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)

    text: Mapped[str] = Column(String(1024), nullable=False)

    # formula_id: Mapped[int] = mapped_column(ForeignKey('formula.id'), nullable=True)

    formula: Mapped['Formula'] = relationship(back_populates='features', lazy=False)

    figure_id: Mapped[int] = mapped_column(ForeignKey('figure.id'), nullable=True)

    figure: Mapped['Figure'] = relationship(back_populates='features')


formula_theorema = Table(
    'formula_theorema',
    BaseModel.metadata,
    Column('formula_id', ForeignKey('formula.id'), primary_key=True),
    Column('theorema_id', ForeignKey('theorema.id'), primary_key=True),
)

# теорема
class Theorema(BaseModel):
    __tablename__ = 'theorema'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(512), nullable=False)

    text = Column(String(1024), nullable=True)

    formulas: Mapped[List["Formula"]] = relationship(secondary=formula_theorema, back_populates='theoremas')

# формула
class Formula(BaseModel):
    __tablename__ = 'formula'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(256), unique=True, nullable=False)

    latex = Column(String(), nullable=True)

    description = Column(String(2048), nullable=True)

    feature_id = mapped_column(ForeignKey('feature.id'), nullable=True)

    theoremas: Mapped[List["Theorema"]] = relationship(secondary=formula_theorema, back_populates='formulas')

    features: Mapped[List["Feature"]] = relationship(back_populates='formula')

# фигура
class Figure(BaseModel):
    __tablename__ = 'figure'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = Column(String(64), unique=True, nullable=False)

    info: Mapped[str] = Column(String(1024), nullable=False)

    plain: Mapped[bool] = Column(Boolean, nullable=False, default=True)

    image: Mapped[str] = Column(String(), nullable=True)

    features: Mapped[List["Feature"]] = relationship(back_populates='figure')
