from dataclasses import KW_ONLY, dataclass, field
from datetime import datetime


@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date




# b1 = Birthday('bhargav', datetime.now())
# TypeError: Birthday.__init__() takes 1 positional argument but 3 were given

b1 = Birthday(name='bhargav', birthday=datetime.now())
print(b1)


@dataclass
class Birthday2:
    name: str
    birthday: datetime.date = field(kw_only=True)


b2 = Birthday('bhargav', birthday=datetime.now())
print(b2)

@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY
    z: float = 0.0
    t: float = 0.0