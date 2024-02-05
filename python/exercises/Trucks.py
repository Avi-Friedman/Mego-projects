class Truck:
    def __init__(self, truck_id, drive_name, num_storage):
        self._truck_id = truck_id
        self.drive_name = drive_name
        self._num_storage = num_storage
        self._is_free = True #difult argoment

    def get_truck_id(self):
        return self._truck_id

    def get_num_storage(self):
        return self._num_storage

    def set_num_storage(self, num_storage):
        self._num_storage = num_storage

    def get_is_free(self):
        return self._is_free

    def set_is_free(self, is_free):
        self._is_free = is_free

truck_1 = Truck(67, "Avi", 8)
truck_2 = Truck(45, "david", 6)
my_list = [truck_1, truck_2]
def check_if_free(lst):
    name_drive_is_free = []
    for i in range(len(lst)):# an addition: for Truck in lst
        if lst[i].num_storage >= 7 and lst[i].is_free == True:
            name_drive_is_free.append(lst[i].drive_name)
    print(f"the drive name is frees {name_drive_is_free}")


def truck_is_bigger_num_storage(lst):
    max_storage_truck = None
    a_big_num_storage = 0

    for item in lst:
        if item.get_is_free() and item.get_num_storage() >= a_big_num_storage:
            max_storage_truck = item
            a_big_num_storage = item.get_num_storage()
    if max_storage_truck is not None:
         print(f"the truck id with max storage is: {max_storage_truck.get_truck_id()} ")
    else:
        print(f"no free track with storage available")

truck_is_bigger_num_storage(my_list)



