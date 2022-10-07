# A simple script which can print the page numbers to print
# Especially helpful when printing multiple pages in a single page
# Developed by Osura Hettiarachchi (<DOVH/>)

print('Welcome to \"Don\'t disturb busy People\"\n')
while (input('Enter \"Q\" to quit OR anything else to proceed: ').upper() != 'Q'):
    number_of_pages_per_page = int(input('Number of pages per page: '))
    total_number_of_pages = int(input('Total number of pages: '))
    start_page = int(input('Staring page number: '))
    y = start_page

    for i in range (total_number_of_pages + 1):
        if i == 0:
            continue;
        elif i >= y and i < (y + number_of_pages_per_page):
            test += str(i) + ',';
        if i == (y + number_of_pages_per_page):
            y += (number_of_pages_per_page * 2);

    print(test[:len(test) -1])
    test = ''

print('Thank you!')
