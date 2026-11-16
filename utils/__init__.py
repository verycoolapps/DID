"""
DID DOCX Generator Utilities Package

Provides utilities for generating professional Design Instructions Documents.

Modules:
    docx_generator: Main DOCX generation engine
    design_formatter: Discipline-specific formatting utilities
"""

from .docx_generator import DIDDocumentGenerator
from .design_formatter import (
    BaseDesignFormatter,
    ArchitecturalFormatter,
    InteriorFormatter,
    GraphicFormatter,
    ThreeDFormatter,
    UIUXFormatter,
    FormatterFactory,
)

__all__ = [
    "DIDDocumentGenerator",
    "BaseDesignFormatter",
    "ArchitecturalFormatter",
    "InteriorFormatter",
    "GraphicFormatter",
    "ThreeDFormatter",
    "UIUXFormatter",
    "FormatterFactory",
]
