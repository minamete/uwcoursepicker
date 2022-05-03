import course

# You can use this to test things
cs_135 = course.Course("cs135", "...", "CS", "Math", "135", "0.5", "W", "", "", "", "")

# offered can be either a list or a NoneType
def parse_offered(offered) -> list:
    """This function changes the format of the 'offered' attribute
    of a course, assumed to be a string of the form "F, W, S" or something similar,
    into a boolean array of length 4"""
    arr = [False, False, False, False]
    # If the offered data is not a string, the offering period is not specified
    if not(isinstance(offered, str)):
        arr[3] = True
        return arr
    # Detection
    for s in offered:
        if s == "F":
            arr[0] = True
        if s == "W":
            arr[1] = True
        if s == "S":
            arr[2] = True
    
    # If the course is not held in any term, it must be held flexibly
    state = True
    for i in arr:
        if i == True:
            state = False
    
    
    arr[3] = state
    return arr

print(parse_offered(cs_135.offered))


