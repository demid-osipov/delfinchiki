#!/usr/bin/env python3

"""
Численное решение задачи скольких-то тел
"""

from __future__ import annotations  # !! typing
from abc import abstractmethod, ABC
from typing import List, Union
from numpy import array as vec
import numpy.linalg
import matplotlib.pyplot as plt

class Body:
    """Тело, движущаееся по двумерной плоскости"""

    def __init__(self, universe: Universe, mass: float, position: vec, velocity: vec):
        # Аннотации типов по желанию, но могут помочь IDE и компилятору, когда таковые имеются
        self.universe: Universe = universe
        self.mass: float = mass
        self.position: vec = position
        self.velocity: vec = velocity

    def force_induced_by_other(self, other: Body) -> vec:
        """Сила, с которой другое тело действует на данное"""
        # Body is forward reference here
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  # Евклидова норма (по теореме Пифагора)
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass *\
                self.universe.gravity_flow_dencity_per_1_1(distance)
        return force

    def advance(self):
        """Перемещаем тело, исходя из его скорости"""
        self.position += self.velocity * MODEL_DELTA_T

    def apply_force(self, force: vec):
        """Изменяем скорость, исходя из силы, действующей на тело"""
        self.velocity += force * MODEL_DELTA_T / self.mass


class Universe(ABC):
    """Невнятная вселенная, основа всех миров"""

    def __init__(self,
                 G: float,  # гравитационная постоянная
                 collision_distance: float  # всё-таки это не точки
                 ):
        self.G: float = G
        self.collision_distance: float = collision_distance


    @abstractmethod
    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
        """
        Плотность потока гравитационного поля между двумя
        единичными массами на заданном расстоянии
        """
        pass

    @abstractmethod
    def model_step(self):
        """Итерация решения задачи Коши. Конечно не присуща вселенной, но тут на своём месте"""
        pass


class UniverseWithBodies(Universe):
    """
    Будем считать, что это наша вселенная. Кстати, в ней тела действуют и
    друг на друга.
    """

    def __init__(self,
                 G: float,  # гравитационная постоянная
                 collision_distance: float  # всё-таки это не точки
                 ):
        super().__init__(G, collision_distance)
        self.bodies: List[Body] = []

    def add_body(self, b: Body):
        self.bodies.append(b)


    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
        return self.G / (
            dist ** 2 if dist > self.collision_distance
            else -self.G / dist ** 3
        )


    def model_step(self):
         for i in range(len(self.bodies)):
            for j in range(len(self.bodies)):
                if i != j:
                    self.bodies[i].apply_force(self.bodies[i].force_induced_by_other(self.bodies[j]))
            self.bodies[i].advance()


if __name__ == '__main__':

    un = UniverseWithBodies(50, 3.0)

    MODEL_DELTA_T = 0.01
    TIME_TO_MODEL = 5

    bodies_arr = []
    bodies_quantity: int = 5
    for i in range(bodies_quantity):
        bodies_arr.append(Body(un, float(30 * i + 10), vec([float(100 * (i/bodies_quantity)), float(-1 ** i * 100 * (i/bodies_quantity))]), vec([float(-1 ** i * -i * bodies_quantity), float(i * bodies_quantity)])))

    for i in range(bodies_quantity):
        un.add_body(bodies_arr[i])

    r = range(int(TIME_TO_MODEL / MODEL_DELTA_T))
        
    x: List[List[float]] = [[0.0] * bodies_quantity for i in r]
    y: List[List[float]] = [[0.0] * bodies_quantity for i in r]

   
    for stepn in r:
        for j in range(bodies_quantity):
            x[stepn][j] = un.bodies[j].position[0]
            y[stepn][j] = un.bodies[j].position[1]
        un.model_step()

    for j in range(bodies_quantity):
        plt.plot(
            [x[stepn][j] for stepn in r],
            [y[stepn][j] for stepn in r]
        )

    plt.show()
