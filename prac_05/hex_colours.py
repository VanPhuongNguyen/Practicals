def main():
    COLOR_NAMES = {'AliceBlue': '#f0f8ff', 'BlanchedAlmond': '#ffebcd', 'BlueViolet': '#8a2be2', 'CadetBlue': '#5f9ea0', 'CornflowerBlue': '#6495ed', 'DarkGoldenrod': '#b8860b', 'DarkGreen': '#006400', 'DarkKhaki': '#bdb76b', 'DarkOrange': '#ff8c00', 'DarkTurquoise': '#00ced1'}
    # Get longest key title
    longest_key_title = max([len(key) for key in COLOR_NAMES])
    for key, value in COLOR_NAMES.items():
        print('{0:<{1}} is {2}'.format(key, longest_key_title, value))

    name = input("Enter color name: ").upper()
    while name:
        if name in COLOR_NAMES:
            print(name, "is", COLOR_NAMES[name])
        else:
            print("Invalid name")
        state = input("Enter color name: ")
 
main() 