
def produce_summary(day_number, file):
    """ to get the produce summary report from a file """
    print("day", day_number)
    delivery_log = open(file)
    for line in delivery_log:
       line = line.rstrip()
       words = line.split('|')

       melon = words[0]
       count = words[1]
       amount = words[2]

       print(f"Delivered {count} {melon}s for total of ${amount}")
    delivery_log.close()
produce_summary(1, "um-deliveries-day-1.txt")
produce_summary(2, "um-deliveries-day-2.txt")
produce_summary(3, "um-deliveries-day-3.txt")