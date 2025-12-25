from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    JSON,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Pattern(Base):
    __tablename__ = "patterns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    designer: Mapped[str | None] = mapped_column(String)
    category: Mapped[str | None] = mapped_column(String)
    skill_level: Mapped[str | None] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(Text)

    created_at: Mapped[str] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    files = relationship("File", back_populates="pattern", cascade="all, delete-orphan")
    metadata_entry = relationship(
        "PatternMetadata",
        back_populates="pattern",
        uselist=False,
        cascade="all, delete-orphan",
    )


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pattern_id: Mapped[int] = mapped_column(ForeignKey("patterns.id"))
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    file_name: Mapped[str] = mapped_column(String, nullable=False)
    file_hash: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    file_type: Mapped[str | None] = mapped_column(String)
    file_size: Mapped[int | None] = mapped_column(Integer)

    added_at: Mapped[str] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    pattern = relationship("Pattern", back_populates="files")


class PatternMetadata(Base):
    __tablename__ = "pattern_metadata"

    pattern_id: Mapped[int] = mapped_column(
        ForeignKey("patterns.id"), primary_key=True
    )
    data: Mapped[dict] = mapped_column(JSON, default=dict)

    pattern = relationship("Pattern", back_populates="metadata_entry")
