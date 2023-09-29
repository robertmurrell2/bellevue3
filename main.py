def feet_to_inches(feet):
  return feet * 3


def main():
  feet = float(input("Enter the number of feet walked: "))
  inches = feet_to_inches(feet)

  print(f"Total feet walked: {feet} inches")
  print(f"Total inches walked: {inches:.2f} inches")


if __name__ == "__main__":
  main()
