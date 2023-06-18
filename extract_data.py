# JSON Imports 
import json
import pprint

# Tkinter Imports
import tkinter as tk
from tkinter import ttk

# Internal Imports
from scrollable_frame import ScrollableFrame
from api import post_mindee_api

# Test API Data from Mindee AI
test_item = '{"api_request": {"error": {}, "resources": ["document"], "status": "success", "status_code": 201, "url": "https://api.mindee.net/v1/products/mindee/expense_receipts/v5/predict"}, "document": {"id": "f0cceb6e-2655-4dac-9b09-8479d62ca0f6", "inference": {"extras": {}, "finished_at": "2023-06-16T18:24:59.899601", "is_rotation_applied": true, "pages": [{"extras": {}, "id": 0, "orientation": {"value": 0}, "prediction": {"category": {"confidence": 0.83, "value": "miscellaneous"}, "date": {"confidence": 0.99, "polygon": [[0.407, 0.192], [0.468, 0.192], [0.468, 0.206], [0.407, 0.206]], "value": "2022-08-04"}, "document_type": {"confidence": 0.99, "value": "EXPENSE RECEIPT"}, "line_items": [{"confidence": 0.77, "description": "94518194563 2022 IOURAUN", "polygon": [[0.342, 0.28], [0.617, 0.277], [0.617, 0.294], [0.342, 0.297]], "quantity": null, "total_amount": 23.99, "unit_price": null}, {"confidence": 0.89, "description": "400001758250 DSGFOUNDAT/N", "polygon": [[0.337, 0.293], [0.618, 0.291], [0.619, 0.308], [0.337, 0.311]], "quantity": null, "total_amount": 0.34, "unit_price": null}, {"confidence": 0.93, "description": "400001001059 1YR1 REPLAC/N", "polygon": [[0.338, 0.308], [0.617, 0.305], [0.617, 0.324], [0.338, 0.326]], "quantity": null, "total_amount": 3.99, "unit_price": null}], "locale": {"confidence": 0.82, "country": "US", "currency": "USD", "language": "en", "value": "en-US"}, "orientation": {"confidence": 0.99, "degrees": 0}, "subcategory": {"confidence": null, "value": null}, "supplier_address": {"confidence": 0.0, "polygon": [], "value": null}, "supplier_company_registrations": [], "supplier_name": {"confidence": 0.96, "polygon": [[0.336, 0.142], [0.648, 0.142], [0.648, 0.168], [0.336, 0.168]], "value": "DICKS SPORTING GOODS"}, "supplier_phone_number": {"confidence": 0.61, "polygon": [[0.438, 0.175], [0.546, 0.175], [0.546, 0.191], [0.438, 0.191]], "value": "(571)2486261"}, "taxes": [{"base": null, "code": "TAX", "confidence": 0.99, "polygon": [[0.338, 0.365], [0.639, 0.365], [0.639, 0.379], [0.338, 0.379]], "rate": null, "value": 1.68}], "time": {"confidence": 0.99, "polygon": [[0.494, 0.191], [0.559, 0.191], [0.559, 0.205], [0.494, 0.205]], "value": "13:24"}, "tip": {"confidence": 0.0, "polygon": [], "value": null}, "total_amount": {"confidence": 0.99, "polygon": [[0.592, 0.406], [0.639, 0.406], [0.639, 0.42], [0.592, 0.42]], "value": 30.0}, "total_net": {"confidence": 0.99, "polygon": [[0.599, 0.353], [0.639, 0.353], [0.639, 0.368], [0.599, 0.368]], "value": 28.32}, "total_tax": {"confidence": 0.99, "polygon": [], "value": 1.68}}}], "prediction": {"category": {"confidence": 0.83, "value": "miscellaneous"}, "date": {"confidence": 0.99, "page_id": 0, "polygon": [[0.407, 0.192], [0.468, 0.192], [0.468, 0.206], [0.407, 0.206]], "value": "2022-08-04"}, "document_type": {"confidence": 0.99, "value": "EXPENSE RECEIPT"}, "line_items": [{"confidence": 0.77, "description": "94518194563 2022 IOURAUN", "page_id": 0, "polygon": [[0.342, 0.28], [0.617, 0.277], [0.617, 0.294], [0.342, 0.297]], "quantity": null, "total_amount": 23.99, "unit_price": null}, {"confidence": 0.89, "description": "400001758250 DSGFOUNDAT/N", "page_id": 0, "polygon": [[0.337, 0.293], [0.618, 0.291], [0.619, 0.308], [0.337, 0.311]], "quantity": null, "total_amount": 0.34, "unit_price": null}, {"confidence": 0.93, "description": "400001001059 1YR1 REPLAC/N", "page_id": 0, "polygon": [[0.338, 0.308], [0.617, 0.305], [0.617, 0.324], [0.338, 0.326]], "quantity": null, "total_amount": 3.99, "unit_price": null}], "locale": {"confidence": 0.82, "country": "US", "currency": "USD", "language": "en", "value": "en-US"}, "subcategory": {"confidence": 0.0, "value": null}, "supplier_address": {"confidence": 0.0, "page_id": null, "polygon": [], "value": null}, "supplier_company_registrations": [], "supplier_name": {"confidence": 0.96, "page_id": 0, "polygon": [[0.336, 0.142], [0.648, 0.142], [0.648, 0.168], [0.336, 0.168]], "value": "DICKS SPORTING GOODS"}, "supplier_phone_number": {"confidence": 0.61, "page_id": 0, "polygon": [[0.438, 0.175], [0.546, 0.175], [0.546, 0.191], [0.438, 0.191]], "value": "(571)2486261"}, "taxes": [{"base": null, "code": "TAX", "confidence": 0.99, "page_id": 0, "polygon": [[0.338, 0.365], [0.639, 0.365], [0.639, 0.379], [0.338, 0.379]], "rate": null, "value": 1.68}], "time": {"confidence": 0.99, "page_id": 0, "polygon": [[0.494, 0.191], [0.559, 0.191], [0.559, 0.205], [0.494, 0.205]], "value": "13:24"}, "tip": {"confidence": 0.0, "page_id": null, "polygon": [], "value": null}, "total_amount": {"confidence": 0.99, "page_id": 0, "polygon": [[0.592, 0.406], [0.639, 0.406], [0.639, 0.42], [0.592, 0.42]], "value": 30.0}, "total_net": {"confidence": 0.99, "page_id": 0, "polygon": [[0.599, 0.353], [0.639, 0.353], [0.639, 0.368], [0.599, 0.368]], "value": 28.32}, "total_tax": {"confidence": 0.99, "page_id": 0, "polygon": [], "value": 1.68}}, "processing_time": 1.387, "product": {"features": ["locale", "category", "subcategory", "document_type", "date", "time", "total_amount", "total_net", "total_tax", "tip", "taxes", "supplier_name", "supplier_company_registrations", "supplier_address", "supplier_phone_number", "orientation", "line_items"], "name": "mindee/expense_receipts", "type": "standard", "version": "5.0"}, "started_at": "2023-06-16T18:24:58.512313"}, "n_pages": 1, "name": "test_receipt.jpg"}}'

calc_row = 0 # Index Row
init_columns = 2 # How many columns before people

number_of_people = 4 # Number of People needed to calculate
checkbox_vars = [] # Array of Checkbox variables

def parse( item ):
    # Load JSON object into an array form
    arr = json.loads( item )

    # Parses the data into a usable form
    useful_data = arr['document']['inference']['pages'][0]['prediction']

    parsed_data = []

    # Grab items listed on the receipt
    purchased_items = []
    for item in useful_data['line_items']:
        i = []
        i.append( {'description': item['description'] } )
        i.append( {'quantity': item["quantity"]})
        i.append( {'total_amount': item['total_amount']}) 
        purchased_items.append(i)

    parsed_data.append( {'items': purchased_items })

    # Append totals to the array
    parsed_data.append( {'total_net': useful_data['total_net']['value'] })
    parsed_data.append( {'total_tax': useful_data['total_tax']['value']})
    parsed_data.append( {'tip': useful_data['tip']['value']})
    parsed_data.append( {'total_amount': useful_data['total_amount']['value']} )

    print( pprint.pprint(parsed_data )) 
    return parsed_data

def checkbox( frame, row ):
    for i in range( init_columns, number_of_people + init_columns ):
        var = tk.IntVar()
        ttk.Checkbutton( frame.scrollable_frame, variable=var, onvalue=1, offvalue=0 ).grid( row = row, column= i )
        checkbox_vars.append( var )

def calculate_division():
    global items

    result = [ var.get() for var in checkbox_vars ]
    matrix = []
    for i in range(0, number_of_people):
        matrix.append( result[i::number_of_people])

    tally = []
    payments = [0] * number_of_people # payment calculations
    divde_by = 0

    for i in range(len(items)):
        divde_by = 0
        item = items[i]
        tally = []
        price = float( item[2]['total_amount'] )
        
        for p in range( len( matrix ) ):
            if matrix[p][i] == 1:
                divde_by += 1
                tally.append(p)

        if len(tally) == 0:
            exit("Cannot have an item with no checks")
        else:
            for p in tally:
                if divde_by != 0:
                    payments[p] += round(price/divde_by, 2)

    print('\n')
    for i in range( len(payments )):
        print( "Person " + str(i + 1) + " owes " + str(payments[i]))

def api_call( FILE_PATH ):
    return post_mindee_api(FILE_PATH).text


if __name__ == "__main__":
    parsed_data = parse( api_call('/Users/calvinjmin/Desktop/test_receipt.jpg') )
    root = tk.Tk()

    frame = ScrollableFrame(root)

    # Init Frame with # of People & Title
    ttk.Label(frame.scrollable_frame, text="Receipt Scanner", font='Helvetica 14 bold').grid(row=0,column=0) 
    ttk.Label(frame.scrollable_frame, text="Item Price", font='Helvetica 14 bold').grid(row=0,column=1) 

    for i in range(init_columns, number_of_people + init_columns):
        ttk.Label(frame.scrollable_frame, text="Person " + str(i - init_columns + 1), font='Helvetica 14 bold' ).grid(row=0,column=i)

    global items
    items = parsed_data[0]['items']
    calc_row += 1

    # Create a frame with checkboxes for the number of people
    for item in items:
        ttk.Label(frame.scrollable_frame, text= item[0]["description"] ).grid(row=calc_row,column=0)
        ttk.Label(frame.scrollable_frame, text= item[2]["total_amount"] ).grid(row=calc_row,column=1)
        checkbox( frame, calc_row )
        calc_row += 1

    ttk.Button( frame.scrollable_frame, text='Calculate', command=calculate_division).grid( row = calc_row, column= 0)

    frame.pack()
    root.mainloop()