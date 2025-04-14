from math import cos, sin, pi
from dataclasses import dataclass
from enum import Enum

Point = float
Distance = float
Angle = float

@dataclass(frozen=True)
class Position:
    x: Point
    y: Point

class CarriageState(Enum):
    UP = "поднята"
    DOWN = "опущена"

class LineColor(Enum):
    BLACK = "черный"
    RED = "красный"
    GREEN = "зелёный"

@dataclass(frozen=True)
class PlotterState:
    position: Position
    angle: Angle
    color: LineColor
    carriage_state: CarriageState

Printer = print 


def draw_line(prt: Printer, from_pos: Position, to_pos: Position, color: LineColor) -> None:
    prt(f"...Чертим линию из ({from_pos.x}, {from_pos.y}) в ({to_pos.x}, {to_pos.y}) используя {color.value} цвет.")

def calc_new_position(distance: Distance, angle: Angle, current: Position) -> Position:
    angle_in_rads = angle * (pi / 180.0)
    x = round(current.x + distance * cos(angle_in_rads))
    y = round(current.y + distance * sin(angle_in_rads))
    return Position(x, y)

def move(prt: Printer, distance: Distance, state: PlotterState) -> PlotterState:
    new_position = calc_new_position(distance, state.angle, state.position)
    if state.carriage_state == CarriageState.DOWN:
        draw_line(prt, state.position, new_position, state.color)
    else:
        prt(f"Передвигаем на {distance} от точки ({state.position.x}, {state.position.y})")
    return PlotterState(new_position, state.angle, state.color, state.carriage_state)

def turn(prt: Printer, angle: Angle, state: PlotterState) -> PlotterState:
    prt(f"Поворачиваем на {angle} градусов")
    new_angle = (state.angle + angle) % 360.0
    return PlotterState(state.position, new_angle, state.color, state.carriage_state)

def carriage_up(prt: Printer, state: PlotterState) -> PlotterState:
    prt("Поднимаем каретку")
    return PlotterState(state.position, state.angle, state.color, CarriageState.UP)

def carriage_down(prt: Printer, state: PlotterState) -> PlotterState:
    prt("Опускаем каретку")
    return PlotterState(state.position, state.angle, state.color, CarriageState.DOWN)

def set_color(prt: Printer, color: LineColor, state: PlotterState) -> PlotterState:
    prt(f"Устанавливаем {color.value} цвет линии.")
    return PlotterState(state.position, state.angle, color, state.carriage_state)

def set_position(prt: Printer, position: Position, state: PlotterState) -> PlotterState:
    prt(f"Устанавливаем позицию каретки в ({position.x}, {position.y}).")
    return PlotterState(position, state.angle, state.color, state.carriage_state)


def draw_triangle(prt: Printer, size: float, state: PlotterState) -> PlotterState:
    state = carriage_down(prt, state)
    for _ in range(3):
        state = move(prt, size, state)
        state = turn(prt, 120.0, state)
    return carriage_up(prt, state)

def draw_square(prt: Printer, size: float, state: PlotterState) -> PlotterState:
    state = carriage_down(prt, state)
    for _ in range(4):
        state = move(prt, size, state)
        state = turn(prt, 90.0, state)
    return carriage_up(prt, state)


def initialize_plotter_state(position: Position, angle: Angle, color: LineColor, carriage_state: CarriageState) -> PlotterState:
    return PlotterState(position, angle, color, carriage_state)

init_position = Position(0.0, 0.0)
init_color = LineColor.BLACK
init_angle = 0.0
init_carriage_state = CarriageState.UP

plotter_state = initialize_plotter_state(init_position, init_angle, init_color, init_carriage_state)

plotter_state = draw_triangle(print, 100.0, plotter_state)

plotter_state = set_position(print, Position(10.0, 10.0), plotter_state)
plotter_state = set_color(print, LineColor.RED, plotter_state)
plotter_state = draw_square(print, 80.0, plotter_state)