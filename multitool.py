import math

def calculate_eirp(tx_power, antenna_gain, loss):
    # Calculate EIRP using the formula: EIRP (dBm) = TX Power (dBm) + Antenna Gain (dBi) - Loss (dB)
    eirp = tx_power + antenna_gain - loss

    # Print the result
    print(f"EIRP: {eirp:.2f} dBm")

if __name__ == "__main__":
    print("Select an option:")
    print("1. Dipole Antenna Calculation")
    print("2. Free-Space Path Loss (FSPL) Calculation")
    print("3. dBm Calculation")
    print("4. EIRP Calculation")

    choice = input("Enter the option (1, 2, 3, or 4): ")

    if choice == "1":
        print("Choose antenna input option:")
        print("1. Predefined bands")
        print("2. Custom frequency in MHz")

        antenna_choice = input("Enter the antenna input option (1 or 2): ")

        if antenna_choice == "1":
            print("Available bands:")
            print("1. 80m")
            print("2. 40m")
            print("3. 20m")
            print("4. 10m")

            band_choice = input("Enter the band choice (1, 2, 3, or 4): ")

            if band_choice == "1":
                frequency = 3.5e6  # 80 meters band frequency in Hz
                calculate_dipole_length(frequency, "80m")
            elif band_choice == "2":
                frequency = 7e6  # 40 meters band frequency in Hz
                calculate_dipole_length(frequency, "40m")
            elif band_choice == "3":
                frequency = 14e6  # 20 meters band frequency in Hz
                calculate_dipole_length(frequency, "20m")
            elif band_choice == "4":
                frequency = 28e6  # 10 meters band frequency in Hz
                calculate_dipole_length(frequency, "10m")
            else:
                print("Invalid band choice.")
        elif antenna_choice == "2":
            frequency = float(input("Enter the frequency in MHz: ")) * 1e6
            calculate_dipole_length(frequency, "")
        else:
            print("Invalid antenna input option.")
    elif choice == "2":
        range_m = float(input("Enter the range between TX/RX in meters: "))
        
        freq_option = input("Choose frequency input option:\n1. MHz\n2. GHz\nEnter the option (1 or 2): ")
        
        if freq_option == "1":
            freq_hz = float(input("Enter the frequency in MHz: ")) * 1e6
        elif freq_option == "2":
            freq_hz = float(input("Enter the frequency in GHz: ")) * 1e9
        else:
            print("Invalid frequency input option.")
            exit(1)

        tx_dbm = float(input("Enter the TX power in dBm: "))
        rx_dbm = float(input("Enter the RX sensitivity in dBm: "))
        calculate_free_space_loss(range_m, freq_hz, tx_dbm, rx_dbm)
    elif choice == "3":
        num_dbm1 = float(input("Enter dBm value 1: "))
        num_dbm2 = float(input("Enter dBm value 2: "))
        calculate_dbm(num_dbm1, num_dbm2)
    elif choice == "4":
        tx_power = float(input("Enter the TX power in dBm: "))
        antenna_gain = float(input("Enter the Antenna Gain in dBi: "))
        loss = float(input("Enter the Loss in dB Cable & Connector Loss : "))
        calculate_eirp(tx_power, antenna_gain, loss)
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
