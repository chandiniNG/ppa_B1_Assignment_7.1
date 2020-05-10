class Parkingdetails():
    def __init__(self, vehicle_number, vehicle_2wheeler, vehicle_4wheeler, entry_time, exit_time):
    	self.vehicle_2wheeler = vehicle_2wheeler
    	self.vehicle_4wheeler = vehicle_4wheeler
    	self.entry_time = entry_time
    	self.exit_time = exit_time

ledger = {}

print("welcome to parking space")

while True:
	print("2_wheeler_slots:six_vacant")
	print("4_wheeler_slots:four_vacant")


	ch = int(input("what type of vehicles you want to park: \n\
                1. 2_wheeler\n\
                2. 4_wheeler")
	print int(input("enter youur choice: "))

	if ch == 1:
		vehicle_number = input("vehicle_number: ")
		entry_time = input("entry_time: ")
		exit_time = input("exit_time: ")

		Parkingdetails = parking(vehicle_number, type_of_vehicle, duration)

		ledger[parking_det] = Parkingdetails

	else ch == 2:
		vehicle_number = input("vehicle_number: ")
		entry_time = input("entry_time: ")
		exit_time = input("exit_time: ")

		parkingdetails = ledger[parking_det]
		parkingdetails.entry_time(time)
		parkingdetails.exit_time()













