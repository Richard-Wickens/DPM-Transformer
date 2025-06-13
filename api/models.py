from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class mTableCell(SQLModel, table=True):
    """
    Represents a single “cell” in a table, identified by both
    CellID and TableID (composite key simulated via two PK fields).
    """
    CellID: int = Field(primary_key=True)
    TableID: int = Field(primary_key=True)
    BusinessCode: str
    DPS: str

class mHierarchy(SQLModel, table=True):
    """
    Represents a hierarchy definition.
    """
    HierarchyID: int = Field(primary_key=True)
    HierarchyCode: str
    HierarchyLabel: str

    # Relationship to the nodes in this hierarchy
    nodes: List["mHierarchyNode"] = Relationship(back_populates="hierarchy")

class mHierarchyNode(SQLModel, table=True):
    """
    Represents a node within a hierarchy, linked back to its parent hierarchy.
    """
    HierarchyNodeID: int = Field(primary_key=True)
    HierarchyID: int = Field(foreign_key="mhierarchy.HierarchyID", primary_key=True)
    Level: int
    Order: int
    HierarchyNodeLabel: str

    # Link back to the MHierarchy
    hierarchy: mHierarchy = Relationship(back_populates="nodes")


