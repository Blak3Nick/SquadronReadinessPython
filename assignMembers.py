
def assign_members(file_to_read):
    members = list()
    with open(file_to_read, 'r') as f:
        for line in f:
            members.append(line.rstrip('\n\t '))
    return members




