import numpy as np
import math

def calculate_sphere_point_of_contact(face, target, r, height):

    x1 = face[0]
    y1 = face[1]
    z1 = face[2] - height

    x2 = target[0]
    y2 = target[1]
    z2 = target[2] - height
    

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    

    a = dx**2 + dy**2 + dz**2
    b = 2 * (dx * x1 + dy * y1 + dz * z1)
    c = x1**2 + y1**2 + z1**2 - r**2
    

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return (0,0,0)

    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    t = min(t1, t2)
    
    x = x1 + t * dx
    y = y1 + t * dy
    z = z1 + t * dz
    
    return (x, y, z)

def calculate_normal_sphere_intersection(face, target, height):
    x1 = face[0]
    y1 = face[1]
    z1 = face[2] - height

    x2 = target[0]
    y2 = target[1]
    z2 = target[2] - height

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    

    dot_product = dx * x1 + dy * y1 + dz * z1
    
    direction_length = math.sqrt(dx**2 + dy**2 + dz**2)

    t = dot_product / direction_length**2
    
    x = t * dx
    y = t * dy
    z = t * dz
    
    return (x, y, z)


def destination(face, target, range, height):
    length = math.sqrt(target[0] ** 2 + target[1] ** 2 + (target[2] - height) ** 2)
    if(target[1] >= 0 and target[2] >= 0):# y > 0 && z > 0 이어야 함
        if(length <= range):#범위안에 있으면
            return target
        else:
            result = np.array([target[0], target[1], target[2] - height])
            result = result * (range/length)
            return result
    else:
        tmp = calculate_sphere_point_of_contact(face,target, range,height)
        if(tmp[1] > 0 and tmp[2] > 0):
            result = np.array(tmp)
            return result
        else:
            tmp = calculate_normal_sphere_intersection(face,target,height)
            tmp1 = np.array(tmp)
            result = tmp1 * (math.sqrt((tmp[0] ** 2 + tmp[1] ** 2 + (tmp[2] - height) ** 2)) / length)
            return result
        