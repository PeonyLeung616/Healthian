import hashlib
import time

#Block layout
class Block: 
    def __init__(self, index, previous_hash, timestamp, patient_id, patient_name, medical_record, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.medical_record = medical_record
        self.hash = hash

# Convert block attributes string into encoded hex string
def calculate_hash(index, previous_hash, timestamp, patient_id, patient_name, medical_record):
    value = str(index) + str(previous_hash) + str(timestamp) + str(patient_id) + str(patient_name) + str(medical_record)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "0", "", "No Medical Records Found", calculate_hash(0, "0", time.time(), "0", "", "No Medical Records Found"))

def create_new_block(previous_block, patient_id, patient_name, medical_record):
    index = previous_block.index + 1
    timestamp = time.time()
    hash_value = calculate_hash(index, previous_block.hash, timestamp, patient_id, patient_name, medical_record)
    return Block(index, previous_block.hash, timestamp, patient_id, patient_name, medical_record, hash_value)

def print_blockchain():
    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Patient ID: {block.patient_id}")
        print(f"Patient Name: {block.patient_name}")
        print(f"Medical Record: {block.medical_record}")
        print(f"Hash: {block.hash}\n")

# Given patient ID to find all the record
def search_patient_by_id(patient_id):
    found_blocks = [block for block in blockchain if block.patient_id == patient_id]
    return found_blocks

# Given patient name to find all the record
def search_patient_by_name(patient_name):
    found_blocks = [block for block in blockchain if block.patient_name.lower() == patient_name.lower()]
    return found_blocks

# Create the blockchain and add the genesis block to the blockchain as first index
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Allow user to add more data for a patient, choose which patient's data to update, add a new patient's data, or search for a patient
while True:
    action = input("Press 'a' to add more data, 'e' to update data, 'n' to add a new patient, 's' to search for a patient, or any other key to exit: ")

    if action == 'a' or action == 'e':
        try:
            patient_id = input("Enter the patient ID: ")
            
            # Find the latest block for the specified patient
            latest_block_for_patient = None
            for block in reversed(blockchain):
                if block.patient_id == patient_id:
                    latest_block_for_patient = block
                    break

            if latest_block_for_patient:
                if action == 'a':
                    new_medical_record = input(f"Enter additional medical record for Patient {patient_id}: ")
                    latest_block_for_patient.medical_record += f"\n{new_medical_record}" if latest_block_for_patient.medical_record != "No Medical Records Found" else new_medical_record
                elif action == 'e':
                    print(f"Current medical record for Patient {patient_id}:\n{latest_block_for_patient.medical_record}")
                    lines = latest_block_for_patient.medical_record.split('\n')
                    line_index = int(input(f"Enter the line number to update (0-{len(lines)-1}): "))
                    if 0 <= line_index < len(lines):
                        new_line_data = input(f"Enter the new medical record for line {line_index}: ")
                        lines[line_index] = new_line_data
                        latest_block_for_patient.medical_record = '\n'.join(lines)
                    else:
                        print("Invalid line number. Update canceled.")
                        continue

                latest_block_for_patient.hash = calculate_hash(latest_block_for_patient.index, latest_block_for_patient.previous_hash, latest_block_for_patient.timestamp, patient_id, latest_block_for_patient.patient_name, latest_block_for_patient.medical_record)
                print(f"Medical record for Patient {patient_id} updated!\n")
                print_blockchain()
            else:
                print(f"No medical records found for Patient {patient_id}. Add a new patient's data.")
        except ValueError:
            print("Invalid input. Please enter a valid patient ID.")
    elif action == 'n':
        patient_id = input("Enter the patient ID for the new patient: ")
        patient_name = input("Enter the name for the new patient: ")
        new_medical_record = input("Enter medical record for the new patient: ")
        new_block = create_new_block(previous_block, patient_id, patient_name, new_medical_record)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"New patient added to the blockchain!")
        print(f"Hash: {new_block.hash}\n")
        print_blockchain()
    elif action == 's':
        search_option = input("Press 'id' to search by patient ID, 'name' to search by patient name: ").lower()
        if search_option == 'id':
            search_id = input("Enter the patient ID to search: ")
            found_blocks = search_patient_by_id(search_id)
        elif search_option == 'name':
            search_name = input("Enter the name of the patient to search: ")
            found_blocks = search_patient_by_name(search_name)
        else:
            print("Invalid search option. Please enter 'id' or 'name'.")
            continue

        if found_blocks:
            print("Found matching patient(s):")
            for block in found_blocks:
                print(f"Index: {block.index}")
                print(f"Timestamp: {block.timestamp}")
                print(f"Patient ID: {block.patient_id}")
                print(f"Patient Name: {block.patient_name}")
                print(f"Medical Record: {block.medical_record}")
                print(f"Hash: {block.hash}\n")
        else:
            print(f"No matching patient found.")
    else:
        break
