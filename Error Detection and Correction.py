# ---------------- PARITY ---------------- #

def generate_parity_bit(data):
    count = data.count('1')
    return '0' if count % 2 == 0 else '1'

def detect_parity_error(sent_data, received_data):
    return generate_parity_bit(sent_data) != generate_parity_bit(received_data)

# ---------------- CRC ---------------- #

def perform_crc_division(data, generator):
    extended_data = data + '0' * (len(generator) - 1)
    data_array = list(extended_data)
    generator_array = list(generator)

    for i in range(len(data_array) - len(generator_array) + 1):
        if data_array[i] == '1':
            for j in range(len(generator_array)):
                data_array[i + j] = str(int(data_array[i + j]) ^ int(generator_array[j]))

    remainder = ''.join(data_array[-(len(generator) - 1):])
    return remainder

def detect_crc_error(sent_data, received_data, crc_result):
    expected_data = sent_data + crc_result
    return expected_data != received_data

# ---------------- HAMMING ---------------- #

def generate_hamming_code(data_bits):
    if len(data_bits) != 4:
        raise ValueError("Only 4-bit data supported for Hamming(7,4).")

    d1, d2, d3, d4 = map(int, data_bits)
    # Calculate parity bits
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    # Arrange as p1 p2 d1 p3 d2 d3 d4
    hamming_code = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
    return hamming_code

def detect_and_correct_hamming_code(code):
    if len(code) != 7:
        raise ValueError("Only 7-bit code supported for Hamming(7,4).")

    bits = list(map(int, code))
    p1 = bits[0]
    p2 = bits[1]
    d1 = bits[2]
    p3 = bits[3]
    d2 = bits[4]
    d3 = bits[5]
    d4 = bits[6]

    c1 = p1 ^ d1 ^ d2 ^ d4
    c2 = p2 ^ d1 ^ d3 ^ d4
    c3 = p3 ^ d2 ^ d3 ^ d4

    error_position = c3 * 4 + c2 * 2 + c1 * 1

    if error_position == 0:
        return "No Error Detected", ''.join(map(str, bits))
    else:
        bits[error_position - 1] ^= 1
        corrected = ''.join(map(str, bits))
        return f"Error at position {error_position} corrected", corrected

# ---------------- MAIN ---------------- #

def main():
    while True:
        print("\nSelect Method:")
        print("1. Parity")
        print("2. CRC")
        print("3. Hamming (7,4)")
        print("4. Exit")
        
        mode = input("Enter choice (1/2/3/4): ").strip()

        if mode == "4":
            print("Exiting the program.")
            break  # Exit the loop

        sent_data = input("Enter Sent Data (binary): ").strip()
        received_data = input("Enter Received Data (binary): ").strip()

        if mode == "1":  # Parity
            parity_bit = generate_parity_bit(sent_data)
            error = detect_parity_error(sent_data, received_data)
            print(f"Parity Bit: {parity_bit}")
            print("Error Detected!" if error else "No Error Detected.")
        
        elif mode == "2":  # CRC
            generator = input("Enter CRC Generator (e.g., 1101): ").strip()
            crc = perform_crc_division(sent_data, generator)
            error = detect_crc_error(sent_data, received_data, crc)
            print(f"CRC: {crc}")
            print("Error Detected!" if error else "No Error Detected.")
        
        elif mode == "3":  # Hamming
            if len(sent_data) == 4 and not received_data:
                hamming = generate_hamming_code(sent_data)
                print(f"Hamming Code: {hamming}")
            elif len(received_data) == 7:
                status, corrected = detect_and_correct_hamming_code(received_data)
                print(f"{status}\nCorrected Code: {corrected}")
            else:
                print("Error: Enter 4-bit sent data for encoding or 7-bit received data for checking.")
        
        else:
            print("Invalid choice. Please select a valid method (1/2/3).")

if __name__ == "__main__":
    main()
