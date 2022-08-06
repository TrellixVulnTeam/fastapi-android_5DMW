from sqlalchemy import table
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from sqlalchemy import UniqueConstraint, Column, String
from datetime import datetime
from pydantic import EmailStr


# class Book(SQLModel, table=True):
#     id:Optional[int]=Field(default=None, primary_key=True)
#     title:str
#     description:str


# class FitnessUserLink(SQLModel, table=True):
#     fitness_id: Optional[int] = Field(
#         default=None, foreign_key="fitness.id", primary_key=True
#     )
#     userpage_id: Optional[int] = Field(
#         default=None, foreign_key="userpage.id", primary_key=True
#     )

class Fitness(SQLModel, table=True):
    # __tablename__='fitness'
    id:Optional[int] = Field(default=None, primary_key = True)
    # email: str = Field(sa_column=Column("email", String, unique=True))
    # fullName: str #Column(String(25), nullable = False, unique = False)
    # passwordFB: str
    
    
    # heroes: List["Hero"] = Relationship(back_populates="team")
    page1Data: List["DataPage1"] = Relationship(back_populates="fitness")
    page3Data: List["DataPage3"] = Relationship(back_populates="fitness")
    page4Data: List["DataPage4"] = Relationship(back_populates="fitness")
    page5Data: List["DataPage5"] = Relationship(back_populates="fitness")
    page6Data: List["DataPage6"] = Relationship(back_populates="fitness")
    page7Data: List["DataPage7"] = Relationship(back_populates="fitness")
    page8Data: List["DataPage8"] = Relationship(back_populates="fitness")
    page9Data: List["DataPage9"] = Relationship(back_populates="fitness")
    page10Data: List["DataPage10"] = Relationship(back_populates="fitness")
    pageuser: List["Userpage"] = Relationship(back_populates="fitness")


class Userpage(SQLModel, table=True):
    # __tablename__='pageuser'
    id:Optional[int] = Field(default=None, primary_key = True)
    email: str = Field(sa_column=Column("email", String, unique=True))
    passwordFB: str = Field(sa_column=Column("passwordFB", String, unique=False))
    fullName: str  = Field(sa_column=Column("fullName", String, unique=False))#Column(String(25), nullable = False, unique = False)
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="pageuser")

# class FitnessRead(Fitness):
#     pass #id: int

# class User(SQLModel, table=True):
#     # __tablename__='datapage1'    
#     id:Optional[int] = Field(default=None, primary_key=True)
#     fullName:str
#     email:str
#     passwordFB:str
#     fitness: Optional[Fitness] = Relationship(back_populates="page1Data")

class DataPage10(SQLModel, table=True):
    # __tablename__='datapage1'    
    id:Optional[int] = Field(default=None, primary_key=True)
    Nothing : bool = False #Column(Boolean, default = False)#": false,
    date : str = "" #Column(Date, nullable = False)#": "May 4, 2022 12:20:55 PM",
    fastFood : bool = False #Column(Boolean, default = False)#": true,
    fastSugar : bool = False #Column(Boolean, default = False)#": false,
    laterNight : bool = False #Column(Boolean, default = False)#": true
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page10Data")

# class DataPage1Read(DataPage1):
#     pass #id: int

# class DataPage1ReadWithFitnes(DataPage1Read):
#     team: Optional[FitnessRead] = None


# class FitnessReadWithDataPage1(FitnessRead):
#     heroes: List[DataPage1Read] = []


class DataPage3(SQLModel, table=True):
    # __tablename__='datapage3'        
    id:Optional[int] = Field(default=None, primary_key = True)
    age : int #Column(Integer, nullable= False)#": 30,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:19:31 PM",
    desired_weight: float #Column(Float(10, 2))#": 50.0,
    height : int #Column(Integer, nullable= False)#": 20,
    weight : float #Column(Float(10, 2))#": 40.0
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page3Data")


class DataPage4(SQLModel, table=True):
    # __tablename__='datapage4'    
    id:Optional[int] = Field(default=None, primary_key = True)
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:25 PM",
    everyDayFitness : bool #Column(Boolean, default = False)#": false,
    examine1_2TimesWeek : bool #Column(Boolean, default = False)#": false,
    examine3_5TimesWeek : bool #Column(Boolean, default = False)#": false,
    fastWalkOnFoot : bool #Column(Boolean, default = False)#": true,
    minimalPhysicalActive : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page4Data")


class DataPage5(SQLModel, table=True):
    # __tablename__='datapage5'        
    id:Optional[int] = Field(default=None, primary_key = True)
    chicken : bool #Column(Boolean, default = False)#": false,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:34 PM",
    fish : bool #Column(Boolean, default = False)#": true,
    meat : bool #Column(Boolean, default = False)#": false,
    pork : bool #Column(Boolean, default = False)#": true,
    seaFood : bool #Column(Boolean, default = False)#": true,
    tyrkey : bool #Column(Boolean, default = False)#": true,
    withoutFish : bool #Column(Boolean, default = False)#": false,
    withoutMeat : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page5Data")


class DataPage6(SQLModel, table=True):
    # __tablename__='datapage6'        
    id:Optional[int] = Field(default=None, primary_key = True)
    avocado : bool #Column(Boolean, default = False)#": false,
    broccoli : bool #Column(Boolean, default = False)#": true,
    cauliflower : bool #Column(Boolean, default = False)#": false,
    cucumbers : bool #Column(Boolean, default = False)#": false,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:42 PM",
    eggplant : bool #Column(Boolean, default = False)#": true,
    mushrooms : bool #Column(Boolean, default = False)#": true,
    tomato : bool #Column(Boolean, default = False)#": true,
    zucchini : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page6Data")


class DataPage7(SQLModel, table=True):
    # __tablename__='datapage7'        
    id:Optional[int] = Field(default=None, primary_key = True)
    cheese : bool #Column(Boolean, default = False)#": true,
    cottage : bool #Column(Boolean, default = False)#": false,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:47 PM",
    egg : bool #Column(Boolean, default = False)#": false,
    kefir : bool #Column(Boolean, default = False)#": false,
    nuts : bool #Column(Boolean, default = False)#": true,
    yogurt : bool #Column(Boolean, default = False)#": true
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page7Data")


class DataPage8(SQLModel, table=True):
    # __tablename__='datapage8'        
    id:Optional[int] = Field(default=None, primary_key = True)
    coffee : bool #Column(Boolean, default = False)#": false,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:50 PM",
    tea : bool #Column(Boolean, default = False)#": false,
    waterSugarGas : bool #Column(Boolean, default = False)#": true,
    waterWithoutGas : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page8Data")


class DataPage9(SQLModel, table=True):
    # __tablename__='datapage9'        
    id:Optional[int] = Field(default=None, primary_key = True)
    InHome : bool #Column(Boolean, default = False)#": false,
    OnFoot : bool #Column(Boolean, default = False)#": false,
    date : str #Column(Date, nullable = False)#": "May 4, 2022 12:20:53 PM",
    regularTraffic : bool #Column(Boolean, default = False)#": true,
    workOffice : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page9Data")


class DataPage1(SQLModel, table=True):
    # __tablename__='datapage10'    
    id:Optional[int] = Field(default=None, primary_key = True)
    man : bool #Column(Boolean, default = False)#": true,
    woman : bool #Column(Boolean, default = False)#": false
    fitness_id:Optional[int] = Field(default=None, foreign_key="fitness.id")
    fitness: Optional[Fitness] = Relationship(back_populates="page1Data")

