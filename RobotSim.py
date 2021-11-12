instructions = "RAALAL"
coords = [7, 3]
direction = "north"
def move(instructions, coords, direction):
    compass = ["north", "east", "south", "west"]
    direction = compass.index(direction)
    for action in instructions:
        match action:
            case 'A':
                match direction:
                    case 0:
                        coords[0] += 1
                    case 1:
                        coords[1] += 1
                    case 2: 
                        coords[0] -= 1
                    case 3:
                        coords[1] -= 1
            case 'R':
                direction = (direction + 1) % 4
            case 'L':
                direction = (direction - 1) % 4
            
        print(coords, "facing", compass[direction])

move(instructions, coords, direction)